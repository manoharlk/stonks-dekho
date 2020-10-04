
from nsepy import get_history
from datetime import date

# from nsepy import get_history
# from datetime import date
import json

# import urllib3
#
# def lambda_handler(event, context):
#     print("The execution of handler is about to START ...")
#     # data = get_history(symbol="SBIN", start=date(2019, 1, 1), end=date(2020, 9, 9))
#     http = urllib3.PoolManager()
#     response = http.request("GET","http://jsonplaceholder.typicode.com/todos/2")
#     print(response.data.decode("utf-8"))
#     print("The execution of handler is about to STOP ...")
#     return {
#         'message': "message"
#     }

from flask import Flask
import nsepy
application = Flask(__name__)


@application.route('/')
def hello():
    print(nsepy.__VERSION__)
    data = get_history(symbol="SBIN", start=date(2020, 9, 9), end=date(2020, 9, 9))
    return str(data)

if __name__ == '__main__':
    application.debug = True
    application.run()