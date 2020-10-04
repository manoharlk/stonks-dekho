
from nsepy import get_history
from datetime import date
from flask import Flask
import nsepy

application = Flask(__name__)

@application.route('/')
def hello():
    print("Request Received!!")
    print(nsepy.__VERSION__)
    data = get_history(symbol="SBIN", start=date(2020, 9, 9), end=date(2020, 9, 9))
    print(data) 
    return str("{message:'hahaha!'}")

if __name__ == '__main__':
    application.debug = True
    application.run(threaded=True, host='0.0.0.0', port=8080, debug=True)
