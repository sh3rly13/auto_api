from requests_oauthlib import OAuth1Session
import os
import json
# In your terminal please set your environment variables by running the following lines of code.

# bu kısımdaki key ve secret api bilgisini değiştiriyoruz.
consumer_key = "xxxxxxxxxFaub6"
consumer_secret = "yyyyyyyyyyyyyyyywQac1f6i7kD469uc7ZaI"


# Get request token
request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

try:
    fetch_response = oauth.fetch_request_token(request_token_url)
except ValueError:
    print(
        "There may have been an issue with the consumer_key or consumer_secret you entered."
    )

resource_owner_key = fetch_response.get("oauth_token")
resource_owner_secret = fetch_response.get("oauth_token_secret")
print("Got OAuth token: %s" % resource_owner_key)

# Get authorization
base_authorization_url = "https://api.twitter.com/oauth/authorize"
authorization_url = oauth.authorization_url(base_authorization_url)
print("Please go here and authorize: %s" % authorization_url)
verifier = input("Paste the PIN here: ")

# Get the access token
access_token_url = "https://api.twitter.com/oauth/access_token"
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=resource_owner_key,
    resource_owner_secret=resource_owner_secret,
    verifier=verifier,
)
oauth_tokens = oauth.fetch_access_token(access_token_url)

access_token = oauth_tokens["oauth_token"]
access_token_secret = oauth_tokens["oauth_token_secret"]

# Make the request
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

# değişiklik yapılan bölümlerin başlangıcı
# Spam algılamaması için günün saat tarihini kullanmak üzere import ettik
from datetime import datetime
import time

while True: # Sürekli olarak bağlantı PIN kodu istememesi için sonsuz döngüye aldık.
    bugun = datetime.now()
    
    # Değişiklik yapılacak kısım
    payload = {"text": "Geri Takip yapılır🫧🟪 \n@gaiminio _:_ https://ranked.gaimin.io?referral=1484298420487704579  \n@GetBlockGames _:_ https://blockgames.app?referral_code=mr.moonrose  \n@GetBubbleCoin _:_ https://bubble.imaginaryones.com/?ref=1UUPRF \n@Metaoasis_ _:_ https://t.me/MomoAI_bot/app?startapp=VLTJHW  \n$BUBBLE #BUBBLE $GMRX #GMRX $ELO #ELO #BLOCK $BLOCK #MOMOAI"+ str(bugun)}


    # Making the request
    response = oauth.post(
        "https://api.twitter.com/2/tweets",
        json=payload,
    )
    if response.status_code != 201:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )
    print("Response code: {}".format(response.status_code))
    # Saving the response as JSON
    json_response = response.json()
    print(json.dumps(json_response, indent=4, sort_keys=True))
    # Yaklaşık 35 dk (2200 sn) da bir olacak şekilde tweet paylaşımı yapıyor. 3600 saniye = 1 saaat
    time.sleep(2200) 