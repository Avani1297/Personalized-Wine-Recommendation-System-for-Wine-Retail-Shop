from flask import Flask, request
from recommendation import recommend_for_customer
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/api/recommendation/recommend", methods = ['POST'])
def recommendapi():
    data = request.get_json()
    if not data :
        return 'invalid input', 400
    if "loyalty_number" not in data.keys() :
        return {'message':'loyalty number not present','status':'Error'}, 400
    if not isinstance(data['loyalty_number'] , list):
        return 'loyalty number must be an array', 400
    if len(data.keys())>1:
         return 'unessasary data', 400
    response = {'status': 'success', 'data':[]}
    for loyalty_number in data['loyalty_number'] :
        response['data'].append({'loyalty_number':loyalty_number, "recommended_products" :recommend_for_customer(loyalty_number)})
        

        
    return response



