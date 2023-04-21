import io
import ast
import os
import urllib.request
import nonebot
from .api_ocr import api_paddle_ocr
from .api_voice import getvoice
from .api_excel import api_paddle_apiexcel
from nonebot import on, on_command, on_notice, on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event, GroupMessageEvent, GroupUploadNoticeEvent,PrivateMessageEvent, NoticeEvent, NotifyEvent, \
    MessageEvent, MessageSegment, Message
from nonebot.internal.rule import Rule
from nonebot.rule import to_me, is_type, command
from nonebot.typing import T_State
from pydantic import BaseSettings




##############################
api_command_config_ = ['apiocr','ocr']
_tome_ = Rule()

try:
    api_command_config_ = eval(nonebot.get_driver().config.apiocr_command)
except:
    api_command_config_ = ['apiocr','ocr']
try:
    if nonebot.get_driver().config.paddle_at:
        if nonebot.get_driver().config.paddle_at == 'True':
            _tome_ = to_me()
except:
    _tome_ = Rule()
api_command = command(*api_command_config_)
##############################

ocr_rule = Rule(api_command)
ocr_api = on(rule=(api_command&_tome_))

@ocr_api.handle()
async def handle_ocr(bot: Bot, event: Event, state: T_State):
    await ocr_api.send("开始apiocr识别模式,支持中英文和数字")


@ocr_api.got("pic")
async def get_pic(bot: Bot, event: Event, state: T_State):
    getmsg = event.get_message()
    for segment in getmsg:
        if segment.type == 'image':
            await ocr_api.send("正在识别~~")
            url = segment.data['url']
            response = urllib.request.urlopen(url)
            img = io.BytesIO(response.read())
            resulttext = await api_paddle_ocr(img=img)
            await ocr_api.reject(resulttext)
        elif segment.type == 'text':
            if getmsg[0].data['text'] == '/结束':
                await ocr_api.finish("关闭ocr识别模式")
            else:
                await ocr_api.send("请发送纯图片，如要结束，请发送/结束")

##############################
try:
    voice_keyword_config_ = eval(nonebot.get_driver().config.apivoice_keyword)
except:
    voice_keyword_config_ = ['/转语音', '/说']
##############################
voice_api = on_keyword({*voice_keyword_config_},rule=_tome_)


@voice_api.handle()
async def handlevoice(bot: Bot, event: Event, state: T_State):
    if bool(event.reply):
        text = event.reply.message[0].data['text']
        url = await getvoice(text)
        record = MessageSegment.record(file=url)
        await voice_api.finish(record)
    else:
        text = event.get_plaintext()
        text = text.replace('/转语音', '').replace('/说', '')
        url = await getvoice(text)
        record = MessageSegment.record(file=url)
        await voice_api.finish(record)



##############################
try:
    excel_command_config_ = eval(nonebot.get_driver().config.apiexcel_command)
except:
    excel_command_config_ = ['excel', '表格']
    
excel_command = command(*excel_command_config_)
##############################

excel_api = on(rule=(excel_command&_tome_))

@excel_api.handle()
async def handle_apiexcel(bot: Bot, event: Event, state: T_State):
    await excel_api.send("开始apiexcel识别模式")

@excel_api.got("")
async def get_pic(bot: Bot, event: Event, state: T_State):
    getmsg = event.get_message()
    for segment in getmsg:
        if segment.type == 'image':
            await excel_api.send("正在识别~~")
            url = segment.data['url']
            resulttext,filename= await api_paddle_apiexcel(url)
            await excel_api.send(resulttext)
            filepath = os.path.dirname(os.path.realpath(__file__)) + r'\temp.xlsx'
            if isinstance(event, GroupMessageEvent) or isinstance(event, GroupUploadNoticeEvent):
                await bot.call_api('upload_group_file', group_id= event.group_id, name=f'{filename}.xlsx', file=filepath)
                await excel_api.reject()
            else:
                await bot.call_api('upload_private_file', user_id= event.user_id, name=f'{filename}.xlsx', file=filepath)
                await excel_api.reject()
        elif segment.type == 'text':
            if getmsg[0].data['text'] == '/结束':
                await excel_api.finish("关闭apiexcel识别模式")
            else:
                await excel_api.send("请发送纯图片，如要结束，请发送/结束")
#######################################                
try: 
    at_ornot = nonebot.get_driver().config.paddle_at
except:
    at_ornot = 'False'
#######################################

help_command = command('paddlehelp','飞桨帮助')               
paddle_help = on(rule=help_command)
@paddle_help.handle()
async def paddle_help1_(bot: Bot, event: Event, state: T_State):
    await paddle_help.finish(f"""
飞桨api功能大全
以下功能是否需要艾特{at_ornot}
1.ocr识别命令:/+{api_command_config_}，发送后进入ocr状态，可连续发图片，输入 /结束 退出
2.表格识别转xlsx功能命令:/+{excel_command_config_},发送后进入表格识别状态，可连续发图片，输入 /结束 退出
3.语音合成功能关键词:{voice_keyword_config_}，消息中有关键词（带/）触发，可以回复他人的消息来生成他人消息的语音
by canxin
                       """)