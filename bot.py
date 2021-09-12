# -*- coding: utf-8 -*-
import telebot
from config import token

@bot.message_handler(func=lambda message: message.forward_from_chat, content_types=["text", "photo", "video"])
def posts_from_channels(msg):
    # Remove messages from blocked groups
    print(msg.chat.title + ' forward')
    if msg.forward_from_chat.id in blocked_groups:
        delete_messge(msg)
        
@bot.message_handler(func=lambda m: True, content_types=['new_chat_members'])
def check_join_messages(msg):
    bot.send_message(msg.chat.id, 'New user joined')
    bot.promote_chat_member(msg.chat.id, msg.from_user.id, is_anonymous=True)


if __name__ == '__main__':
    print("Censoro_bot Started")
    bot.polling(none_stop=True)
