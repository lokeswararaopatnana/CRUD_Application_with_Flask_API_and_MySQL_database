from flask import Flask,jsonify
from mysqlDB import DBhelper
app = Flask(__name__)
db = DBhelper()

@app.route("/")
def trail():
    return "Welcome to CRUD Application"

@app.route("/user/<id>/<username>/<phone>")
def create_user(id,username,phone):
    db.insert_user(id,username,phone)
    data = {
        "id":id,
        "username":username,
        "phone":phone,
    }
    return {"data":data,"status":"Success!","message":"User Created Successfully!"}

@app.route("/users")
def show_users():
    res = db.fetch_all()
    return res

@app.route("/user/<id>")
def fetch_one(id):
    data = db.fetch_one(id)
    if data:
        # data={
        #     "status":"success",
        #     "data":str(data),
        #     "message":"User successfully found!",
        #     "type":str(type(data))
        # }
        return jsonify(data)
    else:
        data = {
            "data":"Data not found!",
            "status":"Status Error!"
        }
        return jsonify(data)

@app.route("/user/del/<userId>")
def delete_user(userId):
    data = db.delete_user(userId)
    if data:
        return data
    else:
        data = {
            "data":"data deleted successfully!",
            "status":"success!"
        }
        return data

@app.route("/user/update/<userId>/<newName>/<newPhone>")
def update_user(userId,newName,newPhone):
    data = db.update_user(userId,newName,newPhone)
    if data:
        return jsonify(data)
    else:
        data = {
            "status":"success!",
            "message":"User updated sucessfully!"
        }
    return data



if __name__ == "__main__":
    app.run(debug=True)