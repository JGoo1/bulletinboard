from flask import Flask
from flask_pymongo import PyMongo
from datetime import datetime

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/bulletinboard" #
mongo = PyMongo(app)

question = mongo.db.question
q1 = {
    "id": 1,
    "subject":"pybo가 무엇인가요?",
    "content":'pybo에 대해서 알고 싶습니다.',
    "create_date" :datetime.now()
}
q2 = {
    "id": 2,
    "subject":"플라스크 모델 질문입니다.",
    "content":'id는 자동으로 생성되나요?',
    "create_date" :datetime.now()
}
question.insert_one(q1)
question.insert_one(q2)

answer = mongo.db.answer
q1 = {
    "id": 1,
    "post_id":2,
    "content":'네, 자동으로 생성됩니다.',
    "create_date" :datetime.now()
}
q2 = {
    "id": 2,
    "post_id":2,
    "content":'id는 키값입니다.',
    "create_date" :datetime.now()
}
answer.insert_one(q1)
answer.insert_one(q2)
print("Success!")