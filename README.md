# Volatility

Sends an email, when the given stock price changes dramatically.
## Prerequisites 
* python3
* pip3 

## Manual Steps 
### In user_cred.py file
* Provide [Tradeking secret keys](https://www.ally.com/api/invest/documentation/oauth/).
* Provide Yahoo email-id and password.


```
# TradeKing Creds
secrets = {"CONSUMER_KEY" : "####",
           "CONSUMER_SECRET" : "####",
           "ACCESS_KEY" : "####",
           "ACCESS_SECRET" : "####"}

# Yahoo Creds
mail_creds = {"SMTP_SERVER" : "smtp.mail.yahoo.com",
              "SMTP_PORT" : 465,
              "SMTP_USERNAME" : "####",
              "SMTP_PASSWORD" : "####",
              "EMAIL_FROM" : "####",
              "EMAIL_TO" : "####"}
 ```

## Run Script
```shell
chmod 777 ./setup.sh
./setup.sh
```

