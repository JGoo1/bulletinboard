from ..database.db_handler import DBHandler
from datetime import datetime

class PostService:
    def __init__(self):
        self.db_handler = DBHandler()
        self.db_name = "bulletinboard"
        self.collection_name= "question"

    def create(self, subject, content):

        data = {
            "id": self.db_handler.get_next_seq(query={"_id": "replyid"}, db_name=self.db_name),
            "subject": subject,
            "content": content,
            "create_date": datetime.now()
        }

        return self.db_handler.insert_item_one(data=data, db_name=self.db_name, collection_name=self.collection_name)

    def delete_post(self):
        pass

    def get_post(self, id):
        return self.db_handler.find_item_one(condition={"id":id}, db_name=self.db_name,collection_name=self.collection_name)

    def get_post_list(self):
        return self.db_handler.find_item(db_name=self.db_name,collection_name=self.collection_name)

    def update_post(self):
        pass
