import json as js
from urllib.request import urlopen
import user_cred as cred
import oauth_util as oauth
import time as time
import collections as coll
import email_utils as ema

def pretty_print(json_obj):
    print(js.dumps(json_obj, indent=4, separators=(',', ': ')))

# response : response json obj
def get_last_price(response):
    return response["response"]["quotes"]["quote"]["last"]

# stock_symbol : string
# secrets: secret map
def get_last_stock_quote(stock_symbol, client):
    timeline_endpoint = "https://api.tradeking.com/v1/market/ext/quotes.json?symbols=" + stock_symbol
    response = client.request(timeline_endpoint)
    if(not response):
        print ("Error : No response from endpoint")
    # response is a tuple.
    # first of tuple : headers
    # second of tuple : response body
    json_obj = js.loads(response[1])
    if (json_obj == None):
        print("Error : The response is not of the expected format")
    return get_last_price(json_obj)

# given an array of numbers, two indexes inside the array, tell if the two numbers are N percent more or less than each other
# returns a map {Bool Number}
def is_more_than_n_percent_different(arr, i, j, n):
    if(arr == None):
        print ("Error : Provide valid list of numbers")
    first = arr[i] if (i>=0) else arr[0]
    second = arr[j] if (j<len(arr)) else arr[len(arr)-1]
    diff = (first-second)
    diff = diff if (diff >= 0) else -diff
    rate_of_change = (diff/first)*100
    print("Log : Rate of change is  : " + str(rate_of_change))
    if(rate_of_change > n):
        return [True, rate_of_change]
    else:
        return [False, rate_of_change]

def append_to_fixed_len_queu(deq, item, fixed_len):
    arr_len = len(deq)
    if(arr_len < fixed_len):
        deq.appendleft(item)
    else:
        deq.pop()
        deq.appendleft(item)
    return deq

def send_email(mail, stock_symbol, rate_of_change):
    email_content = {}
    stock_symbol = "stock_symbol : " + str(stock_symbol) + "\n"
    rate_of_change = "rate_of_change : " + str(rate_of_change) + "\n"

    email_content["BODY"] =  stock_symbol + rate_of_change
    email_content["EMAIL_SUBJECT"] = "**** Stock ALERT ****"
    ema.send_email(mail, email_content)
    print("email sent :" + str(email_content))

def main ():
    stock_symbol = "VVIX"
    client = oauth.get_client(cred.secrets);

    check_stock_gap_time = 60
    max_arr_len = 60
    alert_time = 10*60
    rate_of_change_thresh = 3
    deq = coll.deque([])
    tick = 0
    mail = ema.init_mail()
    while(True):
        time.sleep(1)
        tick = tick + 1
        if(tick >= alert_time):
            tick = 0
            rate_of_change = is_more_than_n_percent_different(deq, 0, max_arr_len-1, rate_of_change_thresh)
            if(rate_of_change[0]):
                print("Rate of change is higher than : " + str(rate_of_change_thresh))
                send_email(mail, stock_symbol, rate_of_change)

        if(tick % check_stock_gap_time == 0):
            # eg: every 1 minute update stock price
            last_price = get_last_stock_quote(stock_symbol, client)
            last_price = float(last_price)
            deq = append_to_fixed_len_queu(deq, last_price, max_arr_len)
            print("Log : Next Tick : " + str(deq))

if(__name__ == "__main__"):
    main()

