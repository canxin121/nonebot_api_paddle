import aiohttp
import asyncio
import base64
import json
import os
from io import BytesIO
from openpyxl import Workbook
from PIL import Image
from html.parser import HTMLParser


async def html2excel(html):
    class MyHTMLParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.data = []
            self.row = []

        def handle_starttag(self, tag, attrs):
            if tag == 'td':
                self.in_td = True

        def handle_endtag(self, tag):
            if tag == 'td':
                self.in_td = False
            elif tag == 'tr':
                self.data.append(self.row)
                self.row = []

        def handle_data(self, data):
            if self.in_td:
                self.row.append(data.strip())

    parser = MyHTMLParser()
    parser.feed(html)
    data = '\n'.join(['\t'.join(row) for row in parser.data])
    return data


async def api_paddle_apiexcel(image_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(image_url) as response:
            img = Image.open(BytesIO(await response.read()))
            buffered = BytesIO()
            img = img.convert('RGB')
            img.save(buffered, format="JPEG")
            img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

            data = {
                "session_hash": "75mq6m01qy4",
                "fn_index": 0,
                "data": [
                    f"data:image/jpeg;base64,{img_str}"
                ]
            }

            headers = {
                'Content-Type': 'application/json',
                'Origin': 'https://aistudio.baidu.com',
                'Accept-Encoding': 'gzip, deflate, br',
                'Cookie': '__bsi=10291592389384054246_00_34_N_R_16_0303_cca8_Y; IMG_WH=428_746; SE_LAUNCH=5%3A1680744441_31%3A28012407_49%3A28012719; PSCBD=31%3A1; BA_HECTOR=2kaha10la18l2104012l8h8v1i2s7vr1m; H_WISE_SIDS=219946_234020_131861_216852_213347_214806_219942_213035_230186_204906_',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Mobile/15E148 Safari/604.1',
                'Referer': 'https://aistudio.baidu.com/serving/app/23/?__theme=light',
                'Content-Length': '195430',
                'Accept-Language': 'zh-CN,zh-Hans;q=0.9'
            }

            url = 'https://aistudio.baidu.com/serving/app/23/run/predict/'

            async with session.post(url, headers=headers, data=json.dumps(data)) as response:
                jsons = json.loads(await response.text())
                result = jsons["data"][0]
                data_excel = await html2excel(result)

                lines = data_excel.strip().split('\n')
                lst = [line.split('\t') for line in lines]
                wb = Workbook()
                ws = wb.active
                for row in lst:
                    ws.append(row)

                filepath = os.path.dirname(os.path.realpath(__file__)) + r'\temp.xlsx'
                wb.save(filepath)

                return data_excel, lst[0][0]