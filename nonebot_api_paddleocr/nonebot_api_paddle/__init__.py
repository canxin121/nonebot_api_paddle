import io
import urllib.request

import requests

from .api_ocr import api_paddle_ocr
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event
from nonebot.rule import to_me
ocr_api = on_command("apiocr", rule=to_me())

@ocr_api.handle()
async def handle_ocr():
    await ocr_api.send("开始apiocr识别模式,支持中英文和数字")


@ocr_api.got("pic")
async def get_pic(event: Event):
    getmsg = event.get_message()
    for segment in getmsg:
        if segment.type == 'image':
            await ocr_api.send("正在识别~~")
            url = segment.data['url']
            try:
                response = urllib.request.urlopen(url)
                img = io.BytesIO(response.read())
                resulttext = api_paddle_ocr(img=img)
                await ocr_api.reject(resulttext)
            except  requests.exceptions.RequestException:
                await ocr_api.send('网络出现错误，下载失败，请重试')

        elif segment.type == 'text':
            if getmsg[0].data['text'] == '/结束':
                await ocr_api.finish("关闭ocr识别模式")
            else:
                await  ocr_api.send("请发送纯图片，如要结束，请发送/结束")
