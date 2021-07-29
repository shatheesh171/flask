import os
from db import db
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from resources.user import UserRegister
from security import authenticate,identity
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app=Flask(__name__)
api=Api(app)
app.secret_key = 'goyala'

#app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL','sqlite:///data.db')
#Changing for heroku, on local run the above one it will automatically pickup sqlite
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://akuotlbooxyuky:d477e6a0f673511b3f62f2fb727a75516af4bdf1c04bc755e17d8a9f84e4222c@ec2-54-73-68-39.eu-west-1.compute.amazonaws.com:5432/d45ung1br13j7t"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList,'/stores')
api.add_resource(UserRegister,'/register')

db.init_app(app)

if __name__=='__main__':
    app.run(debug=True)