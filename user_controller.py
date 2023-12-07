from flask import request
from flask import Flask

from user_model import user_model
obj = user_model()

app = Flask(__name__)


@app.route('/')
def home():
    return "HELLO THIS IS AN API"
      
  

@app.route("/GET/api/books")
def get_all():
    return obj.user_getall()

@app.route("/POST/api/books" , methods = ["POST"])
def addone():
    return obj.user_addone(request.form)


@app.route(f"/PUT/api/books/<int:id>" , methods = ["PUT"])
def update(id):
    return obj.user_update(id ,request.form)

if __name__ == '__main__':
    app.run(debug = True)
