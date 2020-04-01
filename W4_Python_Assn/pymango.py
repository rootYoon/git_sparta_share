from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/orders', methods=['POST'])
def write_order():
    Name = request.form['requestName']
    orderNumNull = request.form['requestOrderNum']
    orderAdd = request.form['requestAdd']
    orderCell = request.form['requestCell']
    db.orders.insert_one({'Name':Name, 'orderNumNull':orderNumNull, 'orderAdd':orderAdd, 'orderCell':orderCell})
    return jsonify({'result': 'success', 'msg': '주문이 완료되었습니다!'})

# data: { "requestName": Name, "requestOrderNum": orderNumNull, "requestAdd": orderAdd, "requestCell": orderCell},

@app.route('/orders', methods=['GET'])
def read_order():
    orders = list(db.orders.find({},{'_id':0}))
    return jsonify({'result':'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)