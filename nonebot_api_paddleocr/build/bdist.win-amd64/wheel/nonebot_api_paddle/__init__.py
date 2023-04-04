import io
import urllib.request
from .api_ocr import api_paddle_ocr
from .api_voice import getvoice
from nonebot import on, on_command, on_notice, on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event, GroupMessageEvent, PrivateMessageEvent, NoticeEvent, NotifyEvent, \
    MessageEvent, MessageSegment, Message
from nonebot.internal.rule import Rule
from nonebot.rule import to_me, is_type, command
from nonebot.typing import T_State

ocr_api = on_command("apiocr", rule=to_me())


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
            resulttext = api_paddle_ocr(img=img)
            await ocr_api.reject(resulttext)
        elif segment.type == 'text':
            if getmsg[0].data['text'] == '/结束':
                await ocr_api.finish("关闭ocr识别模式")
            else:
                await  ocr_api.send("请发送纯图片，如要结束，请发送/结束")


voice_api = on_keyword({'/转语音', '/说'})


@voice_api.handle()
async def handlevoice(bot: Bot, event: Event, state: T_State):
    if bool(event.reply):
        text = event.reply.message[0].data['text']
        url = getvoice(text)
        record = MessageSegment.record(file=url)
        await voice_api.finish(record)
    else:
        text = event.get_plaintext()
        text = text.replace('/转语音', '').replace('/说', '')
        url = getvoice(text)
        record = MessageSegment.record(file=url)
        await voice_api.finish(record)
