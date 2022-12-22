from urllib.parse import parse_qsl, parse_qs
import datetime
from line_chatbot_api import *
import random,json
from foodlist import *

#一開始
def call_service(event):
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://img.onl/3mCuMn',
            title='今天想去哪裡吃?',
            text='請點選想去的地方',
            actions=[
                MessageAction(
                    label='校內餐廳',
                    text='我想在校內餐廳吃!'
                ),
                MessageAction(
                    label='宵夜街',
                    text='我想去宵夜街吃!'
                ),
                MessageAction(
                    label='後門',
                    text='我想去後門吃!'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)
#校內餐廳
def incampus(event):
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            # thumbnail_image_url=url_for('static', filename='images/brown_1024.jpg', _external=True),
            thumbnail_image_url='https://www.cdstm.cn/gallery/zhuanti/ptzt/201711/W020171106647026456045.jpg',
            title='今天想去哪間學餐吃?',
            text='請選擇!',
            actions=[
                PostbackAction(
                    label='男九餐廳',
                    display_text='男九餐廳',
                    data='action=ifood0'
                ),
                PostbackAction(
                    label='松果餐廳',
                    display_text='松果餐廳',
                    data='action=ifood2'
                ),
                PostbackAction(
                    label='松苑餐廳',
                    display_text='松苑餐廳',
                    data='action=ifood1'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)