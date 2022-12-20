from urllib.parse import parse_qsl, parse_qs
import datetime, random, json

from linebot.models import messages
from line_chatbot_api import *
from foodlist import *


def street_brunch(event):
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            # thumbnail_image_url=url_for('static', filename='images/brown_1024.jpg', _external=True),
            thumbnail_image_url='https://i.imgur.com/mfUIthQ.png',
            title='今天我想來點...',
            text='請選擇!',
            actions=[
                PostbackAction(
                    label='主食',
                    display_text='我想吃主食類!',
                    data=f'action=food&item={json.dumps(foodlist[random.randint(0,len(foodlist)-1)])}'
                ),
                PostbackAction(
                    label='小品點心',
                    display_text='我想吃小品點心類!',
                    data=f'action=food&item={json.dumps(foodlist[random.randint(0,len(foodlist)-1)])}'
                ),
                PostbackAction(
                    label='隨機推薦餐點',
                    display_text='隨機推薦餐點小吃',
                    data=f'action=food&item={json.dumps(foodlist[random.randint(0,len(foodlist)-1)])}'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)
def street_dinner(event):
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            # thumbnail_image_url=url_for('static', filename='images/brown_1024.jpg', _external=True),
            thumbnail_image_url='https://i.imgur.com/mfUIthQ.png',
            title='今天我想來點...',
            text='請選擇!',
            actions=[
                PostbackAction(
                    label='主食',
                    display_text='我想吃主食類!',
                    data=f'action=food&item={json.dumps(foodlist[random.randint(0,len(foodlist)-1)])}'
                ),
                PostbackAction(
                    label='小品點心',
                    display_text='我想吃小品點心類!',
                    data=f'action=food&item={json.dumps(foodlist[random.randint(0,len(foodlist)-1)])}'
                ),
                PostbackAction(
                    label='隨機推薦餐點',
                    display_text='隨機推薦餐點小吃',
                    data=f'action=food&item={json.dumps(foodlist[random.randint(0,len(foodlist)-1)])}'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)  

def backdoor_brunch(event):
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            # thumbnail_image_url=url_for('static', filename='images/brown_1024.jpg', _external=True),
            thumbnail_image_url='https://i.imgur.com/mfUIthQ.png',
            title='今天我想來點...',
            text='請選擇!',
            actions=[
                PostbackAction(
                    label='主食',
                    display_text='我想吃主食類!',
                    data=f'action=food&item={json.dumps(foodlist[random.randint(0,len(foodlist)-1)])}'
                ),
                PostbackAction(
                    label='小品點心',
                    display_text='我想吃小品點心類!',
                    data=f'action=food&item={json.dumps(foodlist[random.randint(0,len(foodlist)-1)])}'
                ),
                PostbackAction(
                    label='隨機推薦餐點',
                    display_text='隨機推薦餐點小吃',
                    data=f'action=food&item={json.dumps(foodlist[random.randint(0,len(foodlist)-1)])}'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)
def backdoor_dinner(event):
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            # thumbnail_image_url=url_for('static', filename='images/brown_1024.jpg', _external=True),
            thumbnail_image_url='https://i.imgur.com/mfUIthQ.png',
            title='今天我想來點...',
            text='請選擇!',
            actions=[
                PostbackAction(
                    label='主食',
                    display_text='我想吃主食類!',
                    data=f'action=food&item={json.dumps(foodlist[random.randint(0,len(foodlist)-1)])}'
                ),
                PostbackAction(
                    label='小品點心',
                    display_text='我想吃小品點心類!',
                    data=f'action=food&item={json.dumps(foodlist[random.randint(0,len(foodlist)-1)])}'
                ),
                PostbackAction(
                    label='隨機推薦餐點',
                    display_text='隨機推薦餐點小吃',
                    data=f'action=food&item={json.dumps(foodlist[random.randint(0,len(foodlist)-1)])}'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)  

def show_food(event, food):
    messages=[]
    #messages.append(StickerSendMessage(package_id=foodsticker[0], sticker_id=foodsticker[1]))
    messages.append(TextSendMessage(text=f'為你推薦:{food[1]}，地址:{food[2]}，電話:{food[3]}'))
    messages.append(LocationSendMessage(title=food[1],address=food[2],latitude=food[4],longitude=food[5]))
    line_bot_api.reply_message(event.reply_token, messages)