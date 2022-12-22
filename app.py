# import flask related
from flask import Flask, request, abort, url_for
from urllib.parse import parse_qsl, parse_qs
import random
from linebot.models import events
from line_chatbot_api import *
from service import *
from food import *
# create flask server
app = Flask(__name__)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'

@handler.add(PostbackEvent)
def handle_postback(event):
    user_id = event.source.user_id
    user_name = line_bot_api.get_profile(user_id).display_name
    # print(event.postback.data)
    postback_data = dict(parse_qsl(event.postback.data))
    # print(postback_data.get('action', ''))
    # print(postback_data.get('item', ''))
   


@handler.add(MessageEvent)
def handle_something(event):
    if event.message.type=='text':
        recrive_text=event.message.text
        if '肚子餓' in recrive_text:
            call_service(event)
        elif '我想在校內餐廳吃!' in recrive_text:
            incampus(event) 
        elif '我想去宵夜街吃!' in recrive_text:
            stime(event)
        elif '我想去後門吃!' in recrive_text:
            btime(event)
        else:
            messages=[]
            messages.append(StickerSendMessage(package_id=789, sticker_id=10882))
            messages.append(TextSendMessage(text='抱歉我沒聽懂~ 可以用其他方式再說一次嗎?'))
            line_bot_api.reply_message(event.reply_token, messages)
    elif event.message.type=='sticker':
        receive_sticker_id=event.message.sticker_id
        receive_package_id=event.message.package_id
        line_bot_api.reply_message(event.reply_token, StickerSendMessage(package_id=receive_package_id, sticker_id=receive_sticker_id))


#收到data後要寫什麼讓她可以執行time event
@handler.add(PostbackEvent)
def time(event):
    user_id = event.source.user_id
    user_name = line_bot_api.get_profile(user_id).display_name
    # print(event.postback.data)
    postback_data = dict(parse_qsl(event.postback.data))
    print(postback_data.get('action', ''))
    print(postback_data.get('item', ''))
    postback_data = dict(parse_qsl(event.postback.data))
    print(postback_data.get('action'))
    if postback_data.get('action')=='sb':
        street_brunch(event)
    elif postback_data.get('action')=='sd':
        street_dinner(event)
    elif postback_data.get('action')=='bb':
        backdoor_brunch(event)
    elif postback_data.get('action')=='bd':
        backdoor_dinner(event)
    elif postback_data.get('action')=='ifood0':
        show_food0(event) 
    elif postback_data.get('action')=='ifood1':
        show_food1(event)
    elif postback_data.get('action')=='ifood2':
        show_food2(event)  
    elif postback_data.get('action')=='a':
        a(event) 
    elif postback_data.get('action')=='b':
        b(event)
    elif postback_data.get('action')=='c':
        c(event) 
    elif postback_data.get('action')=='d':
        d(event) 
    elif postback_data.get('action')=='e':
        e(event) 
    elif postback_data.get('action')=='f':
        f(event) 
    elif postback_data.get('action')=='g':
        g(event) 

def stime(event): #宵夜街時間
    confirm_template_message = TemplateSendMessage(
        alt_text='Confirm template',
        template=ConfirmTemplate(
            text='要吃哪餐?',
            actions=[
                PostbackAction(
                    label='早午餐',
                    display_text='我想要吃早午餐!',
                    data='action=sb'
                ),
                PostbackAction(
                    label='晚餐',
                    display_text='我想要吃晚餐!',
                    data='action=sd'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, confirm_template_message)
def btime(event):
    confirm_template_message = TemplateSendMessage(
        alt_text='Confirm template',
        template=ConfirmTemplate(
            text='要吃哪餐?',
            actions=[
                PostbackAction(
                    label='早午餐',
                    display_text='我想要吃早午餐!', 
                    data='action=bb',
                ),
                PostbackAction(
                    label='晚餐',
                    display_text='我想要吃晚餐!',
                    data='action=bd',
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, confirm_template_message) 
def show_food0(event):
    messages=[]
    print(inlist[0][0])
    print(inlist[0][1])
    print(inlist[0][2])
    messages.append(TextSendMessage(text=f'{inlist[0][0]}'))
    messages.append(LocationSendMessage(title='男九餐廳',address='320桃園市中壢區中大路300號國立中央大學校內',latitude=inlist[0][1],longitude=inlist[0][2]))
    line_bot_api.reply_message(event.reply_token, messages)  
def show_food1(event):
    messages=[]
    messages.append(TextSendMessage(text=f'{inlist[1][0]}'))
    messages.append(LocationSendMessage(title='松苑餐廳',address='320桃園市中壢區中大路300號國立中央大學校內',latitude=inlist[1][1],longitude=inlist[1][2]))
    line_bot_api.reply_message(event.reply_token, messages)
def show_food2(event):
    messages=[]
    messages.append(TextSendMessage(text=f'{inlist[2][0]}'))
    messages.append(LocationSendMessage(title='松果餐廳',address='320桃園市中壢區中大路300號國立中央大學校內',latitude=inlist[2][1],longitude=inlist[2][2]))
    line_bot_api.reply_message(event.reply_token, messages)
# run app
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5566, debug=True)