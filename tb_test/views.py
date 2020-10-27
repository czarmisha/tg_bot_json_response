import json

import requests
from django.http import JsonResponse
from django.views import View
from .models import TgUser

TELEGRAM_URL = "https://api.telegram.org/bot"
TUTORIAL_BOT_TOKEN = '1393095899:AAFSSJrU-mTBBCrSCdUF-x6ELQCqa2pXV4g'


# https://api.telegram.org/bot<token>/setWebhook?url=<url>/bot/
class TutorialBotView(View):
    def post(self, request, *args, **kwargs):
        t_data = json.loads(request.body)
        t_message = t_data["message"]
        t_chat = t_message["chat"]
        t_data['text'] = t_data['text'].encode('utf-8')

        TgUser.objects.get_or_create(username=t_chat['username'])
        self.send_message(json.dumps(t_data, indent=4), t_chat["id"])

        return JsonResponse({"ok": "POST request processed"})

    @staticmethod
    def send_message(message, chat_id):
        data = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "Markdown",
        }
        response = requests.post(
            f"{TELEGRAM_URL}{TUTORIAL_BOT_TOKEN}/sendMessage", data=data
        )
