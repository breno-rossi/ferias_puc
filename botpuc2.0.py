## BotPUC 2.0

import datetime
import tweepy 
import time

key =  '1462054983457726469-gREEFEUNo5cUDdUP29hjRaTol5lBg3'  #Acess
secret = 'cwo96KdbpNHLUT5GoZKRNCODecavNTfn9NaKG120OaO62' #Chave secreta

consumer_key = '7YncwJoyMiSuVFaARVTtE4fUS' #API
consumer_secret = 'ZUsTBXatN66WNnqYhzRmpARnPfv54j2MuxfC53sv5lM2r3IieR' #Chave secreta

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth, wait_on_rate_limit=True)


ferias = datetime.date(2022, 6,24) ## Inserir data das férias 
hoje = datetime.date.today()

tempo_falta = ferias - hoje
tempo = tempo_falta.days


if tempo == 1:
    api.update_status("Falta " + str(tempo) + " dia para as férias da PUCPR")
elif tempo == 0: 
    api.update_status("Falta " + str(tempo) + " dia para as férias de PUCPR")
elif tempo != 1:
    api.update_status("Faltam " + str(tempo) + " dias para as férias de PUCPR") 


search = 'Ferias' 'PUCPR'
nrTweets = 50

for tweet in tweepy.Cursor(api.search_tweets, search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(5)
    except StopIteration:
        break

    
    


