from flask import Flask, request
import requests
import random

app = Flask(__name__)

preparedOrder = {
    'order_id': random.randint(1, 10),
    'table_id': random.randint(1, 10),
    'waiter_id': random.randint(1, 10),
    'items': [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)],
    'priority': random.randint(1, 10),
    'max_wait': random.randint(1, 10),
    'pick_up_time': random.randint(1, 60)
}


@app.route("/", methods=['POST'])
def home():
    data = request.form
    order_id = data['order_id']
    table_id = data['table_id']
    waiter_id = data['table_id']
    items = data['table_id']
    priority = data['table_id']
    max_wait = data['table_id']
    pick_up_time = data['table_id']
    print('order_id = ' + order_id + ', table_id = ' + table_id)
    return 'Orders Received'


@app.route('/order')
def order():
    r = requests.post("http://192.168.0.103:5001/", data=preparedOrder)
    return r.text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
