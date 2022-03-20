from flask import Flask,jsonify

app = Flask(__name__)
#POST = used to receive data 
#GET = used to send data back only

stores = [
     {
    'name':'my Wonderful store',
    'items': [
        {
        'name':'My item',
        'price': 989
        }
    ]
}
]
#POST /store data :{name}
@app.route('/store', methods=['POST'])
def create_store():
    pass

#GET /store/<string:name>
@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    pass

#Get store
@app.route('/store', methods=['GET'])
def get_Stores():
    return jsonify({'stores': stores})
    
#POST /store/string:name>/item {name:price}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item(name):
    pass

#GET /store/<string:name/item
@app.route('/store/<string:name>/item', methods=['GET'])
def get_items_in_store(name):
    pass

app.run(port=5000)
