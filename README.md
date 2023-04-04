<p align="center">
<a href="https://github.com/canxin121/nonebot_api_paddleocr"><img src="https://github.com/canxin121/nonebot_paddle_ocr/blob/main/demo/logo_transparent.png" width="200" height="200" alt="nonebot_api_paddle"></a>
</p>
<div align="center">

# nonebot_api_paddle

✨*基于Nonebot的插件，能够将api版本的Paddle OCR接入QQ使用*✨

<div align="left">

## ocr功能
- 支持在群聊和私聊中使用
- 支持连续对话
- 支持中英文和字符  
## 转语音功能
- 将文本内容转化成语音 
## 安装
```
nb plugin install nonebot-api-paddle
```
或者pip安装并添加到pyproject.toml的plugins列表中
```
pip install nonebot-api-paddle
```
## 使用方法

 网页api识别：发送 `/apiocr`，仅支持中英文和数字标点的照片，不可切换语言，发送 `/结束` 即可结束当前用户对话，用户互不影响。
 语音api转换：对想转语音的话回复'/说'或'/转语音'（识别关键词），或者/说 + 内容或/转语音 + 内容

## 示例

| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
|<img src="https://github.com/canxin121/nonebot_paddle_ocr/blob/main/demo/demo%20(3).jpg" width="200">|
|<img src="https://github.com/canxin121/nonebot_paddle_ocr/blob/main/demo/demo%20(3).jpg" width="200">|
## 开源协议

本项目使用了Paddle OCR，并遵守了Apache License 2.0开源协议。
