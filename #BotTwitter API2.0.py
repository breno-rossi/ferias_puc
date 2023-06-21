#BotTwitter API2.0

import datetime
import tweepy


client = tweepy.Client(
    consumer_key="consumer_key",
    consumer_secret="consumer_secret",
    access_token="access_token",
    access_token_secret="access_token_secret",
    bearer_token = "bearer_token",
    wait_on_rate_limit = True,

)



ferias = datetime.date(2023,6,23) ## Inserir data das férias (yyyy\mm\dd)
hoje = datetime.date.today()


tempo_falta = ferias - hoje
tempo = tempo_falta.days


resposta1 = "Falta " + str(tempo) + " dia para as férias da PUCPR"
resposta2 = "Faltam " + str(tempo) + " dias para as férias da PUCPR"



if tempo == 1:
    client.create_tweet(user_auth=True,text=resposta1)
elif tempo == 0:
    client.create_tweet(user_auth=True,text=resposta1)
elif tempo != 1:
    client.create_tweet(user_auth=True,text=resposta2)
