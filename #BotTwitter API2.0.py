#BotTwitter API2.0

import datetime
import tweepy


client = tweepy.Client(
    consumer_key="tBrmO06glzXg0zyf1YZ0ohI5v",
    consumer_secret="zYYVip2jDPTpOjEE53qGJ0X9dJSmDsOVg5hsgwssiT7pf53w8P",
    access_token="1462054983457726469-UG4kaRPUBZUsoaky8UkH6AsePyzqIj",
    access_token_secret="lwl1M7twRglGwFhRkjeNUQsGufzpuO7m6w803PueqvsQ8",
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAHgQnwEAAAAAcYaeyZIDf1FdH%2BiKU3%2FZK3ZC88c%3DPETMAtrkn3xfKMgI9YsIcfWW1l2i3HwX6Ob7YXucVGBu8AnJcR",
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