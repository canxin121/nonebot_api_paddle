import setuptools

with open("readme.rst", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="nonebot_api_paddle",  # 项目名称，保证它的唯一性，不要跟已存在的包名冲突即可
    version="0.1.6",  # 程序版本
    author="canxin",  # 项目作者
    author_email="1969730106@qq.com",  # 作者邮件
    description="nonbot_api_paddle",  # 项目的一句话描述
    long_description=long_description,  # 加长版描述？
    long_description_content_type="text/markdown",  # 描述使用Markdown
    url="https://github.com/canxin121/nonebot_api_paddle",  # 项目地址
    packages=setuptools.find_packages(),  # 无需修改
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU Affero General Public License v3",  # 开源协议
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'nonebot2>=2.0.0rc3',
        'nonebot-adapter-onebot>=2.0.0b1'
        'requests>=2.28.2'
        'ffmpeg>=1.4'
    ]
)
