import firebase_admin
import requests
import asyncio
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
from datetime import datetime
import time
import calendar
import json

mainnet = 'https://api.bscscan.com/'
testnet = 'https://api-testnet.bscscan.com/'
api = '5M6QCQH76TADFIMM39BKR79YZHT6XXG42D'
wallet = '0xEaDA375B9F1B4A39624396cfe3833184b3F817a8'
busd = '0xe9e7cea3dedca5984780bafc599bd69add087d56'
testtoken = '0xf5E6BCf2606f2b610f629b58E1A5Ce4f4Db253DE'
bigtest = '0x84b9b910527ad5c03a9ca831909e21e236ea7b06'
bigtestad = '0xc24c8c4124749dae0d603337a98efadf96d200eb'
contract = testtoken
offset = '10000'
sort = 'asc'
day = 86400/2
delay = 7200
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

async def main():
    cred = credentials.Certificate('./chain-league-8694bded13b2.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    while(True):
        print("Next iteration: " + str(datetime.utcnow()))
        hashList = json.load(open("./hashlist.json", encoding='utf-8'))['list']
        docs = db.collection(u'orders').where(u'state', u'==', u'processing').stream()
        
        meta = db.collection(u'meta').get()[0]
        page = meta.to_dict()['page']
        endpoint = testnet + 'api?module=account&action=tokentx&contractaddress='+ contract + '&address=' + wallet +'&page='+ page + '&offset=' + offset + '&sort=' + sort + '&apikey=' + api

        r = requests.get(endpoint, headers=headers)
        transactions = r.json()['result']
        if(str(len(transactions)) == offset):
            timeTrans = int(transactions[int(offset)-1]['timeStamp'])
            if (abs(timeTrans-int(time.time())) > 100):
                page = str(int(page)+1)
                doc_ref = db.collection(u'meta').document(meta.id)
                doc_ref.update({
                    'page': page, 
                })

        for doc in docs:
            docd = doc.to_dict()
            timeDoc = int(datetime.timestamp(datetime.strptime(docd['time'][2:], '%y-%m-%d %H:%M:%S')))
            found = False
            for transaction in transactions:
                sender = transaction['from'].lower()  
                hashid = transaction['hash']    
                value = int(transaction['value'][0:-18] )   #revisar esto, adaptarlo a la cantidad enviada
                timeTrans = int(transaction['timeStamp'])
                if(sender == docd['wallet'].lower() 
                and value == int(docd['clg'])
                and hashid not in hashList
                and abs(timeDoc-timeTrans) <= day
                and transaction['contractAddress'] == contract.lower()):              
                    hashList.append(hashid)
                    with open( "hashlist.json" , "w" ) as write:
                        json.dump( {"list" : hashList} , write )
                    doc_ref = db.collection(u'orders').document(doc.id)
                    doc_ref.update({
                        'state': "done",
                        'hashid': hashid
                    })
                    #sumar invested
                    doc_ref = db.collection(u'meta').document(meta.id)
                    doc_ref.update({
                        'invested': float(meta.to_dict()['invested']) + int(docd['clg'])*float(docd['clg_price']), 
                    })
                    print("Found")
                    found = True
                    break
            if (not found and abs(timeDoc-int(time.time())) > (day*2)):
                doc_ref = db.collection(u'orders').document(doc.id)
                doc_ref.update({
                    'state': "failed",
                })
                print("Failed")
        time.sleep(delay) 


                
        

if __name__ == '__main__':
  asyncio.run(main())