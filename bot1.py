import requests
import time    
import urllib
import random
from quote import gm,gn
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import xlrd
import os
import emoji
from datetime import datetime
from kec_rn import kec_stud
from googletrans import Translator
from kmail import *
from faculty import *


TOKEN = "740694897:AAF4BzX_dgQKVG9x6iU4JzocAFFwnct-lbY"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
#print('Started')
tt={'Mon':['DAA','1-DBMS 2-JP LAB','1-DBMS 2-JP LAB','1-DBMS 2-JP LAB','OS','JP','SE'],
    'Tue':['DBMS','DAA','DM','JP','SE','DAA-T','OS'],
    'Wed':['JP','OS','DBMS-T','DAA','1-JP 2-OS LAB','1-JP 2-OS LAB','1-JP 2-OS LAB'],
    'Thu':['SE','1-OS 2-DBMS LAB','1-OS 2-DBMS LAB','1-OS 2-DBMS LAB','JP','DBMS','DM'],
    'Fri':['DM','DBMS','OS','SE','DAA','DM','DBMS'],
    'Sat':['DM','PT','PT','LIB','COUNS','SEM','SPD']
    }
print('Started')
def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    return  requests.get(url).json()

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url=URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    try:
        r=requests.get(url,timeout=30)
        if r.reason!='OK':print(r.text)
        print('Msg Sent')
    except Exception as e:
        print(e)
        print(url)
def sendImage(fileName,chat_id):
    url = URL + "sendPhoto";
    files = {'photo': open(fileName, 'rb')}
    data = {'chat_id' : chat_id}
    try:
        r= requests.post(url, files=files, data=data)
        if r.reason!='OK':print(r.text)
    except Exception as e:
        print(e)
        print(url)

def main():
    last_update_id = None
    while True:
        try:
            updates = get_updates(last_update_id)           
            z=updates.get("result")
            if z and len(z) > 0:
                last_update_id = get_last_update_id(updates) + 1
                echo_all(updates)
            time.sleep(0.5)
        except Exception as e:
            print(e)        
def echo_all(updates):

    for update in updates["result"]:
        try:
            print(update)
            chat = update["message"]["chat"]["id"]
            a = update["message"].get("text")
            if a: print(chat,a)
            msg=a
            if msg.lower().startswith('t.'):
                a=msg[2:]
                try:
                    translator = Translator()
                    t=translator.translate(a,dest='ta')
                    msg=str(t.text)
                except Exception as e:
                    msg='Error Caused'
            #if msg.lower()=='tt':
            #    try:
            #        msg=str(tt[datetime.now().strftime("%a")])[1:-1]
            #    except Exception as e:
            #        msg='Error Caused'
            #if msg.lower()=='tta':
            #    try:
            #        msg=str(tta[datetime.now().strftime("%a")])[1:-1]
            #    except Exception as e:
            #        msg='Error Caused'
            #if msg.lower()=='tt.full':
            #    msg=str(tt)
            if msg.lower().startswith('hi') or msg.lower().split()[0] in ['hello','helo']:
                msg='Hi I am Rajee Bot Created by Shareek 😊'
            if msg.lower().startswith('oi'):
                msg='Oi baby'
            if any(i in msg.lower().split() for i in ['luv','love']):
                msg='💘'
            if msg.lower().startswith('ok'):
                msg=emoji.emojize(':thumbs_up:')
            if msg[:-3]=='17csr' or '17csl' or '17cst':
                try:
                    loc = (os.path.join(".","CS.xlsx"))
                    wb = xlrd.open_workbook(loc) 
                    sheet = wb.sheet_by_index(0)
                    for i in range(1,254):
                        if sheet.cell_value(i,0).lower()==msg.lower():
                            sm=''
                            if sheet.cell_value(i,4).lower() == 'male':
                                sm='boy'
                                msg='Name :'+sheet.cell_value(i,3)+' '+emoji.emojize(':'+sm+':')+'\ne-mail :'+sheet.cell_value(i,16)+'\nPh : +91'+str(int(sheet.cell_value(i,15)))
                            else:
                                sm='girl'
                                msg='Name :'+sheet.cell_value(i,3)+' '+emoji.emojize(':'+sm+':')+'\ne-mail :'+sheet.cell_value(i,16)
                except Exception as e:
                    msg='Error Caused'
            if msg[:-3]=='16csr' or '16csl' or '16cst':
                try:
                    loc = (os.path.join(".","CS16.xlsx"))
                    wb = xlrd.open_workbook(loc) 
                    sheet = wb.sheet_by_index(0)
                    for i in range(1,234):
                        if sheet.cell_value(i,0).lower()==msg.lower():
                            sm=''
                            if sheet.cell_value(i,4).lower() == 'male':
                                sm='boy'
                                msg='Name :'+sheet.cell_value(i,3)+' '+emoji.emojize(':'+sm+':')+'\ne-mail :'+sheet.cell_value(i,16)+'\nPh : +91'+str(int(sheet.cell_value(i,15)))
                            else:
                                sm='girl'
                                msg='Name :'+sheet.cell_value(i,3)+' '+emoji.emojize(':'+sm+':')+'\ne-mail :'+sheet.cell_value(i,16)
                except Exception as e:
                    msg='Error Caused'
            if msg[:-3]=='17eer' or '17eel':
                try:
                    loc = (os.path.join(".","EE.xlsx"))
                    wb = xlrd.open_workbook(loc) 
                    sheet = wb.sheet_by_index(0)
                    for i in range(1,sheet.nrows):
                        if sheet.cell_value(i,0).lower()==msg.lower():
                            sm=''
                            if sheet.cell_value(i,4).lower() == 'male':
                                sm='boy'
                                msg='Name :'+sheet.cell_value(i,3)+' '+emoji.emojize(':'+sm+':')+'\ne-mail :'+sheet.cell_value(i,16)+'\nPh : +91'+str(int(sheet.cell_value(i,15)))
                            else:
                                sm='girl'
                                msg='Name :'+sheet.cell_value(i,3)+' '+emoji.emojize(':'+sm+':')+'\ne-mail :'+sheet.cell_value(i,16)
                except Exception as e:
                    msg='Error Caused'
            if msg[:-3]=='16eer' or '16eel':
                try:
                    loc = (os.path.join(".","EE16.xlsx"))
                    wb = xlrd.open_workbook(loc) 
                    sheet = wb.sheet_by_index(0)
                    for i in range(1,sheet.nrows):
                        if sheet.cell_value(i,0).lower()==msg.lower():
                            sm=''
                            if sheet.cell_value(i,4).lower() == 'male':
                                sm='boy'
                                msg='Name :'+sheet.cell_value(i,3)+' '+emoji.emojize(':'+sm+':')+'\ne-mail :'+sheet.cell_value(i,16)+'\nPh : +91'+str(int(sheet.cell_value(i,15)))
                            else:
                                sm='girl'
                                msg='Name :'+sheet.cell_value(i,3)+' '+emoji.emojize(':'+sm+':')+'\ne-mail :'+sheet.cell_value(i,16)
                except Exception as e:
                    msg='Error Caused'
        
            if msg.lower().startswith('s.'):
                msg1=''
                try:
                    for i,j in zip(kec_stud.keys(),kec_stud.values()):
                        if msg.lower()[2:] in j.lower():
                            #print(i+" --> "+j)
                            msg1=msg1+i+' --> '+j+'\n'
                    msg=msg1
                except Exception as e:
                    msg='Error Caused'
            if msg.lower()=='gm' or msg.lower().split()[0] in ['good','gud'] and msg.lower().split()[1] in ['morning','mrng']:
                msg=random.choice(gm)+' 🌤️'
            if msg.lower()=='gn' or msg.lower().split()[0] in ['good','gud'] and msg.lower().split()[1] in ['night','nyt']:
                msg=random.choice(gn)+' 🌟'
            if msg.lower().startswith('r.'):
                d=msg.lower()
                for i,j in zip(kec_stud.keys(),kec_stud.values()):
                    if i.lower()==d[2:] :
                        msg=i+'-->'+j
                msg=msg+'\nmail:'+rectify(d[2:])
            if msg.lower().startswith('cs.'):
                a='No faculty'
                a=getFaccs(msg[3:])
                msg=a
            if msg.lower().startswith('ec.'):
                a='No faculty'
                a=getFacec(msg[3:])
                msg=a
            if msg.lower().startswith('ce.'):
                a='No faculty'
                a=getFacce(msg[3:])
                msg=a
            if msg.lower().startswith('me.'):
                a='No faculty'
                a=getFacme(msg[3:])
                msg=a
            if msg.lower().startswith('ee.'):
                a='No faculty'
                a=getFacee(msg[3:])
                msg=a
            if msg.lower().startswith('it.'):
                a='No faculty'
                a=getFacit(msg[3:])
                msg=a
            if msg.lower().startswith('ei.'):
                a='No faculty'
                a=getFacei(msg[3:])
                msg=a
            if msg.lower().startswith('mt.'):
                a='No faculty'
                a=getFacmt(msg[3:])
                msg=a
            if msg.lower().startswith('ch.'):
                a='No faculty'
                a=getFacch(msg[3:])
                msg=a
            if msg.lower().startswith('ft.'):
                a='No faculty'
                a=getFacft(msg[3:])
                msg=a
            if msg.lower().startswith('au.'):
                a='No faculty'
                a=getFacau(msg[3:])
                msg=a
            if msg.lower().startswith('eng.'):
                a='No faculty'
                a=getFaceng(msg[4:])
                msg=a
            if msg.lower().startswith('che.'):
                a='No faculty'
                a=getFacche(msg[4:])
                msg=a
            if msg.lower().startswith('phy.'):
                a='No faculty'
                a=getFacphy(msg[4:])
                msg=a
            if msg.lower().startswith('mat.'):
                a='No faculty'
                a=getFacmat(msg[4:])
                msg=a
            if(msg.lower().split()[0] in ['how','hw'] and msg.lower().split()[1] in ['are','r'] and msg.lower().split()[2] in ['you','u']):
                msg='Fine buddy 😊\nwhat about you..?'
            if 'hate' in msg.lower().split():
                msg='Love is the building block for all relationships... 💕'
        
            send_message(msg,chat)             
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()
