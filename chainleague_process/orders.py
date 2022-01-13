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
ico = {
    11: [0.0025, 2000000],
    12: [0.0030, 5000000],
    13: [0.0035, 7000000],
    14: [0.0040, 9000000],
    21: [0.0045, 10000000],
    22: [0.0050, 11000000],
    23: [0.0055, 12000000],
    24: [0.0060, 13000000],
    31: [0.0065, 14000000],
    32: [0.0070, 15000000],
    33: [0.0075, 16000000],
    34: [0.0080, 17000000],
    41: [0.0085, 18000000],
    42: [0.0090, 19000000],
    43: [0.0095, 20000000],
    44: [0.0100, 21000000],
    51: [0.0105, 22000000],
    52: [0.0110, 23000000],
    53: [0.0115, 24000000],
    54: [0.0120, 25000000],
    61: [0.0125, 26000000],
    62: [0.0130, 27000000],
    63: [0.0135, 28000000],
    64: [0.0140, 28000000],
    71: [0.0145, 29000000],
    72: [0.0150, 29000000],
    73: [0.0155, 30000000],
}
async def main():
    cred = credentials.Certificate('./chain-league-8694bded13b2.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    while(True):
        print("Next iteration: " + str(datetime.utcnow()))
        hashList = json.load(open("./hashlist.json", encoding='utf-8'))['list']
        ordersList = json.load(open("./orders.json", encoding='utf-8'))
        docs = db.collection(u'orders').where(u'state', u'==', u'processing').stream()
        meta = db.collection(u'meta').get()[0]
        page = meta.to_dict()['page']
        phase_tokens = meta.to_dict()['phase_tokens']
        phase = meta.to_dict()['phase']
        endpoint = testnet + 'api?module=account&action=tokentx&contractaddress='+ contract + '&address=' + wallet +'&page='+ page + '&offset=' + offset + '&sort=' + sort + '&apikey=' + api

        r = requests.get(endpoint, headers=headers)
        transactions = r.json()['result']
        if(str(len(transactions)) == offset):
            timeTrans = int(transactions[int(offset)-1]['timeStamp'])
            if (abs(timeTrans-int(time.time())) > delay):
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
                value = int(transaction['value'][0:-18] )   
                timeTrans = int(transaction['timeStamp'])
                if(sender == docd['wallet'].lower() 
                #and value == int(docd['clg']) adaptarlo a la cantidad enviada
                and hashid not in hashList
                and abs(timeDoc-timeTrans) <= day
                and transaction['contractAddress'] == contract.lower()):   
                    userTokens = value/float(docd['clg_price']) 
                    hashList.append(hashid)
                    with open( "hashlist.json" , "w" ) as write:
                        json.dump( {"list" : hashList} , write )
                    
                    #Comprobacion fase
                    if(userTokens + phase_tokens >= ico[phase][1]):
                        #Primer order
                        doc_ref = db.collection(u'orders').document(doc.id)
                        doc_ref.update({
                            'state': "done",
                            'hashid': hashid,
                            'clg' : abs(ico[phase][1] - phase_tokens)
                        })
                        ordersList[doc.id] = {
                            'state': "done",
                            'hashid': hashid,
                            'clg' : abs(ico[phase][1] - phase_tokens),
                            'clg_price': docd['clg_price'],
                            'wallet' : docd['wallet'],
                            'user': docd['user'],
                            'time': docd['time']
                        }
                        phase_tokens = abs(ico[phase][1] - (userTokens + phase_tokens))
                        i = list(ico).index(phase) + 1
                        phase = list(ico)[i]
                        skips = True                        
                        while(skips):
                            if(phase_tokens >= ico[phase][1]):
                                #Crear nuevos orders
                                newId = db.collection(u'orders').add({
                                    'state': "done",
                                    'hashid': hashid,
                                    'clg' : ico[phase][1],
                                    'clg_price': ico[phase][0],
                                    'wallet' : docd['wallet'].lower() ,
                                    'user': docd['user'],
                                    'time': docd['time'] ,
                                })
                                ordersList[newId] = {
                                    'state': "done",
                                    'hashid': hashid,
                                    'clg' : ico[phase][1],
                                    'clg_price': ico[phase][0],
                                    'wallet' : docd['wallet'].lower() ,
                                    'user': docd['user'],
                                    'time': docd['time'] ,
                                }                                
                                phase_tokens = abs(ico[phase][1] - phase_tokens)
                                i = list(ico).index(phase) + 1
                                phase = list(ico)[i]
                            else:
                                #Crear nuevos orders
                                newId = db.collection(u'orders').add({
                                    'state': "done",
                                    'hashid': hashid,
                                    'clg' : phase_tokens,
                                    'clg_price': ico[phase][0],
                                    'wallet' : docd['wallet'].lower() ,
                                    'user': docd['user'],
                                    'time': docd['time'] ,
                                })
                                ordersList[newId] = {
                                    'state': "done",
                                    'hashid': hashid,
                                    'clg' : phase_tokens,
                                    'clg_price': ico[phase][0],
                                    'wallet' : docd['wallet'].lower() ,
                                    'user': docd['user'],
                                    'time': docd['time'] ,
                                } 
                                skips = False   
                    else:
                        phase_tokens = phase_tokens + userTokens
                        #Primer order
                        doc_ref = db.collection(u'orders').document(doc.id)
                        doc_ref.update({
                            'state': "done",
                            'hashid': hashid,
                            'clg' : userTokens
                        })
                        ordersList[doc.id] = {
                            'state': "done",
                            'hashid': hashid,
                            'clg' : userTokens,
                            'clg_price': docd['clg_price'],
                            'wallet' : docd['wallet'],
                            'user': docd['user'],
                            'time': docd['time']
                        }
                    # referral tokens
                    userRef = db.collection(u'users').document(docd['user']).get().to_dict()
                    if (userRef['referal'] != ""):
                        db.collection(u'orders').add({
                            'state': "done",
                            'hashid': "referral",
                            'clg' : userTokens/10,
                            'clg_price': docd['clg_price'],
                            'wallet' : "referral",
                            'user': userRef['referal'][4:],
                            'time': docd['time'] 
                        })                   
                    with open( "orders.json" , "w" ) as write:
                        json.dump( ordersList , write )
                    #sumar invested y editar phase
                    doc_ref = db.collection(u'meta').document(meta.id)
                    doc_ref.update({
                        'invested': float(meta.to_dict()['invested']) + value, 
                        'phase' : phase,
                        'phase_tokens' : phase_tokens
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