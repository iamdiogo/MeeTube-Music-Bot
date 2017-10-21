from __future__ import unicode_literals
from telegram import *
from telegram.ext import *
from random import randint
from html.parser import HTMLParser
from bs4 import BeautifulSoup
from lxml import etree
import urllib.request, json, requests, time, urllib.parse, os, urllib, lxml, youtube_dl

GET_CDICE = range(1)
GET_DOWNLOADMUSIC1, GET_DOWNLOADMUSIC2 = range(2)

def start(bot, update):
    update.message.reply_text(
        "Hiiiiiii!\nI'm Mr. MeeTube, look at me!\n"
        "So, what can you do?\n\n"
        "/song - Get a song from YouTube!\n"
        "\nMiscellaneous:\n"
        "/coin - Flip a coin\n"
        "/dice - Roll a dice\n"
        "/cdice - Roll a custom dice")

def asksong(bot, update):
    update.message.reply_text("What's the song you're looking for?")
    return GET_DOWNLOADMUSIC1

def downloadmusic(bot, update, user_data):
    lastmsg = update.message.text
    update.message.reply_text('Searching...')
    try:
        query = urllib.parse.quote(lastmsg)
        url = ("https://www.youtube.com/results?sp=EgIQAQ%253D%253D&q={}".format(query))
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")

        titles = []
        links = []
        for n in range(0,3):
            linkyt = soup.findAll(attrs={'class':'yt-uix-tile-link'})[n]['href'].replace("watch?v=","")
            truelink = 'https://youtu.be' + linkyt
            links.append(truelink)
            class MyHTMLParser(HTMLParser):
                def handle_starttag(self, tag, attrs):
                    if tag == 'title':
                        self.found = True

                def handle_data(self, data):
                    if self.found == True:
                        titles.append(data.replace(' - YouTube',''))
                        self.found = False

            fp = urllib.request.urlopen(truelink)
            mybytes = fp.read()

            mystr = mybytes.decode("utf8")
            fp.close()

            parser = MyHTMLParser()
            parser.found = False
            parser.feed(mystr)

        messagetosend = 'Please select a number:\n'
        i = 1
        for n in titles:
            messagetosend += '{}. {}\n'.format(i, n)
            i += 1
        messagetosend = messagetosend.strip()
        update.message.reply_text(messagetosend)

        user_data['titles'] = titles
        user_data['links'] = links

        return GET_DOWNLOADMUSIC2
    except:
        update.message.reply_text('An error ocurred. Sorry for the inconvenience')
        return ConversationHandler.END


def downloadmusic_response(bot, update, user_data):
    user = update.message.from_user['username']
    lastmsg = update.message.text
    choice = 0
    if lastmsg.strip() == '1':
        choice = 0
    elif lastmsg.strip() == '2':
        choice = 1
    elif lastmsg.strip() == '3':
        choice = 2
    else:
        update.message.reply_text("That isn't an option. Please choose 1, 2 or 3.")
        return GET_DOWNLOADMUSIC2

    musictitle = user_data['titles'][choice]
    musiclink = user_data['links'][choice]

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '{}/music.mp3'.format(user),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        update.message.reply_text('Downloading...')
        ydl.download([musiclink])

    if os.path.getsize('{}/music.mp3'.format(user)) < 50000000:
        os.rename('{}/music.mp3'.format(user),'{}/{}.mp3'.format(user,musictitle))
        update.message.reply_text('Okay, here it is!')
        bot.send_audio(chat_id=update.message.chat_id, audio=open('{}/{}.mp3'.format(user,musictitle), 'rb'))
    else:
        update.message.reply_text("I'm sorry but the song you requested is larger than telegram's max size limit, 50MB")
    os.remove('{}/{}.mp3'.format(user,musictitle))
    return ConversationHandler.END

def coin(bot, update):
    options = ['heads (cara)', 'tails (coroa)']
    c = randint(0,1)
    update.message.reply_text("Coin flipped!\nCame out {}".format(options[c]))

def dice(bot, update):
    f = randint(1,6)
    update.message.reply_text("Dice rolled!\nCame out {}".format(str(f)))

def cdice(bot, update):
    update.message.reply_text("Please send me a number")

    return GET_CDICE

def cdice_response(bot, update):
    number = update.message.text
    number = number.strip()
    # Here you have the number in variable number

    # Implement HERE custom dice responde
    update.message.reply_text("Custom dice rolled!\nCame out {}".format(randint(1, number)))

    return ConversationHandler.END

def error(bot, update, error):
    print('Update "{}" caused error "{}"'.format(update, error))
    return ConversationHandler.END

def main():
    api_key = "INSERT HERE YOUR OWN"
    updater = Updater(api_key)
    dp = updater.dispatcher

    # Commands for the bot
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("coin", coin))
    dp.add_handler(CommandHandler("dice", dice))


    cdice_handler = ConversationHandler(
        entry_points=[CommandHandler('cdice', cdice)],

        states={
            GET_CDICE: [MessageHandler(Filters.text, cdice_response)],
        },
        fallbacks=[MessageHandler(Filters.text,
                                           cdice_response,
                                           pass_user_data=True),
                            ]
    )

    dp.add_handler(cdice_handler)

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('song', asksong)],

        states={
            GET_DOWNLOADMUSIC1: [MessageHandler(Filters.text, downloadmusic, pass_user_data=True)],
            GET_DOWNLOADMUSIC2: [MessageHandler(Filters.text, downloadmusic_response, pass_user_data=True)],
        },
        fallbacks=[MessageHandler(Filters.text,
                                           error,
                                           pass_user_data=True),
                            ]
    )
    dp.add_handler(conv_handler)

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
