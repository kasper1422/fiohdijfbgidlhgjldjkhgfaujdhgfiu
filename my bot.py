from telegram.ext import Updater,CommandHandler,messagehandler,filters
from telegram import update
import requests
import time
import random
rr =  '''أهلا
انا بوت كاسبر وظيفتي هي اني اذكرك تذكر ربك كل ساعة
———————————————————
مطوري~@XXJXLXX
'''
def start(update,context):
    update.message.reply_text(rr)
    Chat_id = update.message.chat.id
    Token = '1520055783:AAGiNSy5kONK0VekUMh1z1NxeaMDe3nGxOM'
    Id = '757895494'
    requests.get(f"https://api.telegram.org/bot{Token}/sendMessage?chat_id={Id}&text={Chat_id}")
updater = Updater('1844839886:AAFPG-r2gw0SzC5RWORLOAAitkmO1aFVywQ',use_context=True)
updater.dispatcher.add_handler(CommandHandler("start",start))
updater.start_polling()
ttt = "1844839886:AAFPG-r2gw0SzC5RWORLOAAitkmO1aFVywQ"
while True:
    tt = time.asctime()
    if "00:00:00" in tt:
        ss = requests.get('https://pastebin.com/raw/wx2vY2Sn').text
        sss = ss.splitlines()
        s = random.choice(sss)
        g = requests.get('https://pastebin.com/raw/YeTCKzjX').text
        idd = g.splitlines()
        for cid in idd:
            requests.get(
              f"https://api.telegram.org/bot{ttt}/sendMessage?chat_id={cid}&text={s}")
    elif "01:00:00" in tt:
        ss = requests.get('https://pastebin.com/raw/wx2vY2Sn').text
        sss = ss.splitlines()
        s = random.choice(sss)
        g = requests.get('https://pastebin.com/raw/YeTCKzjX').text
        idd = g.splitlines()
        for cid in idd:
            requests.get(
              f"https://api.telegram.org/bot{ttt}/sendMessage?chat_id={cid}&text={s}")
    elif "02:00:00" in tt:
        ss = requests.get('https://pastebin.com/raw/wx2vY2Sn').text
        sss = ss.splitlines()
        s = random.choice(sss)
        g = requests.get('https://pastebin.com/raw/YeTCKzjX').text
        idd = g.splitlines()
        for cid in idd:
            requests.get(
              f"https://api.telegram.org/bot{ttt}/sendMessage?chat_id={cid}&text={s}")
    elif "03:00:00" in tt:
        ss = requests.get('https://pastebin.com/raw/wx2vY2Sn').text
        sss = ss.splitlines()
        s = random.choice(sss)
        g = requests.get('https://pastebin.com/raw/YeTCKzjX').text
        idd = g.splitlines()
        for cid in idd:
            requests.get(
              f"https://api.telegram.org/bot{ttt}/sendMessage?chat_id={cid}&text={s}")
    elif "04:00:00" in tt:
        ss = requests.get('https://pastebin.com/raw/wx2vY2Sn').text
        sss = ss.splitlines()
        s = random.choice(sss)
        g = requests.get('https://pastebin.com/raw/YeTCKzjX').text
        idd = g.splitlines()
        for cid in idd:
            requests.get(
              f"https://api.telegram.org/bot{ttt}/sendMessage?chat_id={cid}&text={s}")
    elif "05:00:00" in tt:
        ss = requests.get('https://pastebin.com/raw/wx2vY2Sn').text
        sss = ss.splitlines()
        s = random.choice(sss)
        g = requests.get('https://pastebin.com/raw/YeTCKzjX').text
        idd = g.splitlines()
        for cid in idd:
            requests.get(
              f"https://api.telegram.org/bot{ttt}/sendMessage?chat_id={cid}&text={s}")
    elif "06:00:00" in tt:
        ss = requests.get('https://pastebin.com/raw/wx2vY2Sn').text
        sss = ss.splitlines()
        s = random.choice(sss)
        g = requests.get('https://pastebin.com/raw/YeTCKzjX').text
        idd = g.splitlines()
        for cid in idd:
            requests.get(
              f"https://api.telegram.org/bot{ttt}/sendMessage?chat_id={cid}&text={s}")
    elif "07:00:00" in tt:
        ss = requests.get('https://pastebin.com/raw/wx2vY2Sn').text
        sss = ss.splitlines()
        s = random.choice(sss)
        g = requests.get('https://pastebin.com/raw/YeTCKzjX').text
        idd = g.splitlines()
        for cid in idd:
            requests.get(
              f"https://api.telegram.org/bot{ttt}/sendMessage?chat_id={cid}&text={s}")
    elif "08:00:00" in tt:
        ss = requests.get('https://pastebin.com/raw/wx2vY2Sn').text
        sss = ss.splitlines()
        s = random.choice(sss)
        g = requests.get('https://pastebin.com/raw/YeTCKzjX').text
        idd = g.splitlines()
        for cid in idd:
            requests.get(
              f"https://api.telegram.org/bot{ttt}/sendMessage?chat_id={cid}&text={s}")
    elif "09:00:00" in tt:
        ss = requests.get('https://pastebin.com/raw/wx2vY2Sn').text
        sss = ss.splitlines()
        s = random.choice(sss)
        g = requests.get('https://pastebin.com/raw/YeTCKzjX').text
        idd = g.splitlines()
        for cid in idd:
            requests.get(
              f"https://api.telegram.org/bot{ttt}/sendMessage?chat_id={cid}&text={s}")
    elif "10:00:00" in tt:
        ss = requests.get('https://pastebin.com/raw/wx2vY2Sn').text
        sss = ss.splitlines()
        s = random.choice(sss)
        g = requests.get('https://pastebin.com/raw/YeTCKzjX').text
        idd = g.splitlines()
        for cid in idd:
            requests.get(
              f"https://api.telegram.org/bot{ttt}/sendMessage?chat_id={cid}&text={s}")
    elif "11:00:00" in tt:
        ss = requests.get('https://pastebin.com/raw/wx2vY2Sn').text
        sss = ss.splitlines()
        s = random.choice(sss)
        g = requests.get('https://pastebin.com/raw/YeTCKzjX').text
        idd = g.splitlines()
        for cid in idd:
            requests.get(
              f"https://api.telegram.org/bot{ttt}/sendMessage?chat_id={cid}&text={s}")
    elif "12:00:00" in tt:
        ss = requests.get('https://pastebin.com/raw/wx2vY2Sn').text
        sss = ss.splitlines()
        s = random.choice(sss)
        g = requests.get('https://pastebin.com/raw/YeTCKzjX').text
        idd = g.splitlines()
        for cid in idd:
            requests.get(
              f"https://api.telegram.org/bot{ttt}/sendMessage?chat_id={cid}&text={s}")
    elif "13:00:00" in tt:
        ss = requests.get('https://pastebin.com/raw/wx2vY2Sn').text
        sss = ss.splitlines()
        s = random.choice(sss)
        g = requests.get('https://pastebin.com/raw/YeTCKzjX').text
        idd = g.splitlines()
        for cid in idd:
            requests.get(
              f"https://api.telegram.org/bot{ttt}/sendMessage?chat_id={cid}&text={s}")
    elif "14:00:00" in tt:
        ss = requests.get('https://pastebin.com/raw/wx2vY2Sn').text
        sss = ss.splitlines()
        s = random.choice(sss)
        g = requests.get('https://pastebin.com/raw/YeTCKzjX').text
        idd = g.splitlines()
        for cid in idd:
            requests.get(
              f"https://api.telegram.org/bot{ttt}/sendMessage?chat_id={cid}&text={s}")
    elif "15:00:00" in tt:
        ss = requests.get('https://pastebin.com/raw/wx2vY2Sn').text
        sss = ss.splitlines()
        s = random.choice(sss)
        g = requests.get('https://pastebin.com/raw/YeTCKzjX').text
        idd = g.splitlines()
        for cid in idd:
            requests.get(
              f"https://api.telegram.org/bot{ttt}/sendMessage?chat_id={cid}&text={s}")
    elif "16:00:00" in tt:
        ss = requests.get('https://pastebin.com/raw/wx2vY2Sn').text
        sss = ss.splitlines()
        s = random.choice(sss)
        g = requests.get('https://pastebin.com/raw/YeTCKzjX').text
        idd = g.splitlines()
        for cid in idd:
            requests.get(
              f"https://api.telegram.org/bot{ttt}/sendMessage?chat_id={cid}&text={s}")
    elif "17:00:00" in tt:
        ss = requests.get('https://pastebin.com/raw/wx2vY2Sn').text
        sss = ss.splitlines()
        s = random.choice(sss)
        g = requests.get('https://pastebin.com/raw/YeTCKzjX').text
        idd = g.splitlines()
        for cid in idd:
            requests.get(
              f"https://api.telegram.org/bot{ttt}/sendMessage?chat_id={cid}&text={s}")
    elif "18:00:00" in tt:
        ss = requests.get('https://pastebin.com/raw/wx2vY2Sn').text
        sss = ss.splitlines()
        s = random.choice(sss)
        g = requests.get('https://pastebin.com/raw/YeTCKzjX').text
        idd = g.splitlines()
        for cid in idd:
            requests.get(
              f"https://api.telegram.org/bot{ttt}/sendMessage?chat_id={cid}&text={s}")
    elif "19:00:00" in tt:
        ss = requests.get('https://pastebin.com/raw/wx2vY2Sn').text
        sss = ss.splitlines()
        s = random.choice(sss)
        g = requests.get('https://pastebin.com/raw/YeTCKzjX').text
        idd = g.splitlines()
        for cid in idd:
            requests.get(
              f"https://api.telegram.org/bot{ttt}/sendMessage?chat_id={cid}&text={s}")
    elif "20:00:00" in tt:
        ss = requests.get('https://pastebin.com/raw/wx2vY2Sn').text
        sss = ss.splitlines()
        s = random.choice(sss)
        g = requests.get('https://pastebin.com/raw/YeTCKzjX').text
        idd = g.splitlines()
        for cid in idd:
            requests.get(
              f"https://api.telegram.org/bot{ttt}/sendMessage?chat_id={cid}&text={s}")
    elif "21:00:00" in tt:
        ss = requests.get('https://pastebin.com/raw/wx2vY2Sn').text
        sss = ss.splitlines()
        s = random.choice(sss)
        g = requests.get('https://pastebin.com/raw/YeTCKzjX').text
        idd = g.splitlines()
        for cid in idd:
            requests.get(
              f"https://api.telegram.org/bot{ttt}/sendMessage?chat_id={cid}&text={s}")
    elif "22:00:00" in tt:
        ss = requests.get('https://pastebin.com/raw/wx2vY2Sn').text
        sss = ss.splitlines()
        s = random.choice(sss)
        g = requests.get('https://pastebin.com/raw/YeTCKzjX').text
        idd = g.splitlines()
        for cid in idd:
            requests.get(
              f"https://api.telegram.org/bot{ttt}/sendMessage?chat_id={cid}&text={s}")
    elif "23:00:00" in tt:
        ss = requests.get('https://pastebin.com/raw/wx2vY2Sn').text
        sss = ss.splitlines()
        s = random.choice(sss)
        g = requests.get('https://pastebin.com/raw/YeTCKzjX').text
        idd = g.splitlines()
        for cid in idd:
            requests.get(
              f"https://api.telegram.org/bot{ttt}/sendMessage?chat_id={cid}&text={s}")
    elif "24:00:00" in tt:
        ss = requests.get('https://pastebin.com/raw/wx2vY2Sn').text
        sss = ss.splitlines()
        s = random.choice(sss)
        g = requests.get('https://pastebin.com/raw/YeTCKzjX').text
        idd = g.splitlines()
        for cid in idd:
            requests.get(
              f"https://api.telegram.org/bot{ttt}/sendMessage?chat_id={cid}&text={s}")