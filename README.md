<p align="center">
<a href="https://github.com/canxin121/nonebot_api_paddleocr"><img src="https://github.com/canxin121/nonebot_paddle_ocr/blob/main/demo/logo_transparent.png" width="200" height="200" alt="nonebot_api_paddle"></a>
</p>
<div align="center">

# nonebot_api_paddle

✨*基于Nonebot的插件，能够将api版本的Paddle OCR接入QQ使用*✨

<div align="left">
## 帮助菜单
- 输入'/paddle'或'/飞桨帮助'即可获取所有操作的命令
## ocr功能
- 支持在群聊和私聊中使用
- 支持连续对话
- 支持中英文和字符  
## 转语音功能  
- 将文本内容转化成语音   
## 表格图转文件功能  
- 将图片中的表格还原到文件中  
## 安装
```
nb plugin install nonebot-api-paddle
```
或者pip安装并添加到pyproject.toml的plugins列表中
```
pip install nonebot-api-paddle
```
## 配置（在.env or .env.dav中修改）
以下配置为默认配置，如不需修改可以不写  

```
#ocr命令  
apiocr_command = ['ocr','apiocr']             
#语音合成关键词  
apivoice_keyword = ['/说','/转语音']         
#表格识别命令
apiexcel_command = ['excel','表格']        
#功能是否需要at机器人，只有为True时为需要，任意值为不需要
paddle_at = False
```
## 使用方法
 帮助菜单：输入'/paddle'或'/飞桨帮助'即可获取所有操作的命令  
 网页api识别：输入ocr的命令后，连续发送图片进行识别，仅支持中英文和数字标点的照片，不可切换语言，发送 `/结束` 即可结束当前用户对话，用户互不影响。 
 语音api转换：对想转语音的话回复识别关键词，或者识别关键词 + 内容  
 表格api识别：输入ocr的命令后，连续发送图片进行识别，发送 `/结束` 即可结束当前用户对话，用户互不影响。 
## 示例

| Image 1 | Image 2 |
|:-------:|:-------:|
| ![](https://github.com/canxin121/nonebot_api_paddle/blob/main/demo/demo.png) | ![](https://github.com/canxin121/nonebot_api_paddle/raw/main/demo/demo.jpg) |

## 开源协议

本项目使用了Paddle OCR，并遵守了Apache License 2.0开源协议。
