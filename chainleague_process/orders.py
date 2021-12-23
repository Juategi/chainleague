import firebase_admin
import requests
import asyncio
from firebase_admin import credentials
from firebase_admin import firestore
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
contract = testtoken
offset = '10000'
page = '1'
sort = 'asc'
day = 86400/2
endpoint = testnet + 'api?module=account&action=tokentx&contractaddress='+ contract + '&address=' + wallet +'&page='+ page + '&offset=' + offset + '&sort=' + sort + '&apikey=' + api
async def main():
    cred = credentials.Certificate('./chain-league-8694bded13b2.json')
    firebase_admin.initialize_app(cred)
    hashList = json.load(open("./hashlist.json", encoding='utf-8'))['list']
    db = firestore.client()
    docs = db.collection(u'orders').where(u'state', u'==', u'processing').stream()
   
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    r = requests.get(endpoint, headers=headers)
    transactions = r.json()['result']
    
    for doc in docs:
        docd = doc.to_dict()
        timeDoc = int(datetime.timestamp(datetime.strptime(docd['time'][2:], '%y-%m-%d %H:%M:%S')))
        found = False
        for transaction in transactions:
            sender = transaction['from'].lower()  
            hashid = transaction['hash']    
            value = int(transaction['value'][0:-18] )   
            timeTrans = int(transaction['timeStamp'])
            if(sender == docd['wallet'].lower() 
            and value == int(docd['clg'])
            and hashid not in hashList
            and abs(timeDoc-timeTrans) <= day
            and transaction['contractAddress'] == contract.lower()):              
                hashList.append(hashid)
                print(hashList)
                with open( "hashlist.json" , "w" ) as write:
                    json.dump( {"list" : hashList} , write )
                doc_ref = db.collection(u'orders').document(doc.id)
                doc_ref.set({
                    'user': docd['user'],
                    'clg': docd['clg'],          
                    'clg_price': docd['clg_price'],
                    'state': "done",
                    'time': docd['time'],
                    'wallet': docd['wallet'], 
                    'hashid': hashid
                })
                print("Found")
                found = True
                break
        if (not found and abs(timeDoc-int(time.time())) > (day*2)):
            doc_ref = db.collection(u'orders').document(doc.id)
            doc_ref.set({
                'user': docd['user'],
                'clg': docd['clg'],          
                'clg_price': docd['clg_price'],
                'state': "failed",
                'time': docd['time'],
                'wallet': docd['wallet'], 
            })
            print("Failed")


                
        

if __name__ == '__main__':
  asyncio.run(main())