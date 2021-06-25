from ..database.db_handler import DBHandler
from datetime import datetime

class ReplyService:
    def __init__(self):
        self.db_handler = DBHandler()
        self.db_name =  "bulletinboard"
        self.collection_name = "reply"

    def create(self, post_id, content):

        data = {
            "id": self.db_handler.get_next_seq(query={"_id": "replyid"}, db_name=self.db_name),
            "post_id": post_id,
            "content": content,
            "create_date": datetime.now()
        }

        return self.db_handler.insert_item_one(data=data, db_name=self.db_name, collection_name=self.collection_name)


    def delete_reply(self):
        pass

    def get_reply(self, id, post_id):
        return self.db_handler.find_item_one(condition={"id": id, "post_id": post_id},
                                             db_name=self.db_name,collection_name=self.collection_name)

    def get_reply_list(self, post_id):
        return self.db_handler.find_item(condition={"post_id": post_id},
                                         db_name=self.db_name,collection_name=self.collection_name)

    def update_reply(self):
        pass
