from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, 
    PostbackEvent,
    TextMessage, 
    TextSendMessage, 
    ImageSendMessage, 
    StickerSendMessage, 
    LocationSendMessage,
    TemplateSendMessage,
    ButtonsTemplate,
    PostbackAction,
    MessageAction,
    URIAction,
    CarouselTemplate,
    CarouselColumn,
    ImageCarouselTemplate,
    ImageCarouselColumn,
    DatetimePickerAction,
    ConfirmTemplate
)

line_bot_api = LineBotApi('PCIMInfE0DgPqekRaYeag/titcKt4PnnMwfb9MPdzHlOYb9yrn93oxzAOo3aLjgEVF7YrK4kFymct6b342yLX08NjZFMDpwOe31pfLgSpf3fbbPkXdQ/OPn0aHhTQePogSeX9bsdX2mmY8XHQMXWqgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('79dfffc747f927b0f2b44097e895d507')