from urllib.parse import parse_qsl, parse_qs
import datetime, random, json

from linebot.models import messages
from line_chatbot_api import *
from foodlist import *


def street_brunch(event):
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://ubernewsroomapi.10upcdn.com/wp-content/uploads/2021/06/960x540_01.png',
            title='今天我想來點...',
            text='請選擇!',
            actions=[
                PostbackAction(
                    label='主食',
                    display_text='我想吃主食類!',
                    data='action=a'
                ),
                PostbackAction(
                    label='小品點心',
                    display_text='我想吃小品點心類!',
                    data='action=b'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)
def street_dinner(event):
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://ubernewsroomapi.10upcdn.com/wp-content/uploads/2021/06/960x540_01.png',
            title='今天我想來點...',
            text='請選擇!',
            actions=[
                PostbackAction(
                    label='主食',
                    display_text='我想吃主食類!',
                    data='action=a'
                ),
                PostbackAction(
                    label='小品點心',
                    display_text='我想吃小品點心類!',
                    data='action=c'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)  

def backdoor_brunch(event):
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://ubernewsroomapi.10upcdn.com/wp-content/uploads/2021/06/960x540_01.png',
            title='今天我想來點...',
            text='請選擇!',
            actions=[
                PostbackAction(
                    label='主食',
                    display_text='我想吃主食類!',
                    data='action=d'
                ),
                PostbackAction(
                    label='小品點心',
                    display_text='我想吃小品點心類!',
                    data='action=e'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)
def backdoor_dinner(event):
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://ubernewsroomapi.10upcdn.com/wp-content/uploads/2021/06/960x540_01.png',
            title='今天我想來點...',
            text='請選擇!',
            actions=[
                PostbackAction(
                    label='主食',
                    display_text='我想吃主食類!',
                    data='action=f'
                ),
                PostbackAction(
                    label='小品點心',
                    display_text='我想吃小品點心類!',
                    data='action=g'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)  

def a(event,):
    messages=[]
    messages.append(TextSendMessage(text='為你推薦'))
    messages.append(LocationSendMessage(title=streetblists[random.randint(0,len(streetblists)-1)][0],address='-',latitude=streetblists[random.randint(0,len(streetblists)-1)][1],longitude=streetblists[random.randint(0,len(streetblists)-1)][2]))
    line_bot_api.reply_message(event.reply_token, messages)
def b(event):
    messages=[]
    messages.append(TextSendMessage(text='為你推薦'))
    messages.append(LocationSendMessage(title=sslist[random.randint(0,len(sslist)-1)][0],address='-',latitude=sslist[random.randint(0,len(sslist)-1)][1],longitude=sslist[random.randint(0,len(sslist)-1)][2]))
    line_bot_api.reply_message(event.reply_token, messages)
def c(event):
    messages=[]
    messages.append(TextSendMessage(text='為你推薦'))
    messages.append(LocationSendMessage(title=streetdlist[random.randint(0,len(streetdlist)-1)][0],address='-',latitude=streetdlist[random.randint(0,len(streetdlist)-1)][1],longitude=streetdlist[random.randint(0,len(streetdlist)-1)][2]))
    line_bot_api.reply_message(event.reply_token, messages)
def d(event):
    messages=[]
    messages.append(TextSendMessage(text='為你推薦'))
    messages.append(LocationSendMessage(title=foodlists[random.randint(0,len(foodlists)-1)][0],address='-',latitude=foodlists[random.randint(0,len(foodlists)-1)][1],longitude=foodlists[random.randint(0,len(foodlists)-1)][2]))
    line_bot_api.reply_message(event.reply_token, messages)
def e(event):
    messages=[]
    messages.append(TextSendMessage(text='為你推薦'))
    messages.append(LocationSendMessage(title=backdlist[random.randint(0,len(backdlist)-1)][0],address='-',latitude=backdlist[random.randint(0,len(backdlist)-1)][1],longitude=backdlist[random.randint(0,len(backdlist)-1)][2]))
    line_bot_api.reply_message(event.reply_token, messages)
def f(event):
    messages=[]
    messages.append(TextSendMessage(text='為你推薦'))
    messages.append(LocationSendMessage(title=foodlist[random.randint(0,len(foodlist)-1)][0],address='-',latitude=foodlist[random.randint(0,len(foodlist)-1)][1],longitude=foodlist[random.randint(0,len(foodlist)-1)][2]))
    line_bot_api.reply_message(event.reply_token, messages)
def g(event):
    messages=[]
    messages.append(TextSendMessage(text='為你推薦'))
    messages.append(LocationSendMessage(title=backdlist[random.randint(0,len(backdlist)-1)][0],address='-',latitude=backdlist[random.randint(0,len(backdlist)-1)][1],longitude=backdlist[random.randint(0,len(backdlist)-1)][2]))
    line_bot_api.reply_message(event.reply_token, messages)