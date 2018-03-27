import tweepy,random, time

CONSUMER_KEY = #Your consumer key
CONSUMER_SECRET = #Your Secret
ACCESS_KEY = #keep the quotes, replace this with your access token
ACCESS_SECRET = #keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

listaIDs= []

#Add accounts to the List, example:

listaIDs.append("flanchota")
listaIDs.append("Mufalsa")
listaIDs.append("vamoatwittea")
listaIDs.append("elcosodelapizza")


#Stops following every follower that doesn't follow back
a= api.friends_ids(id="soyunfernet_")
b= api.followers_ids(id="soyunfernet_")

for e in a:
    if e not in b:
        print (e)
        api.destroy_friendship(id=e)


#Tweets

for i in range (0,100):


    #Chooses the user
    user = random.choice(listaIDs)
    #Takes 20 latest's Tweets
    twits = api.user_timeline(id=user)
    #Picks one at random
    t= random.choice(twits)

    ok=False
    while (ok==False):
        if (t.truncated != True) and (t.text[:2] != "RT") and (t.source != "Instagram") and (t.in_reply_to_user_id == None):
            print (t.text.encode("utf-8"))
            api.update_status(t.text)
            ok=True

            si = random.randint (1,3)
            if (si==2):
                usr = random.randint(7,15)
                for follower in tweepy.Cursor(api.followers, id=user).items(usr):
                    follower.follow()
        else:
            t= random.choice(twits)

    #sets the sleep interval
    cc = random.randint(300,1200)
    time.sleep(cc)

