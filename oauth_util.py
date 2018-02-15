import oauth2 as oauth

def get_consumer(secrets):
    return oauth.Consumer(key=secrets["CONSUMER_KEY"], secret=secrets["CONSUMER_SECRET"])

def get_access_token(secrets):
    return oauth.Token(key=secrets["ACCESS_KEY"], secret=secrets["ACCESS_SECRET"])

def get_client(secrets):
    consumer = get_consumer(secrets)
    access_token = get_access_token(secrets)
    return oauth.Client(consumer, access_token)