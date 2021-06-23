from ..database.db_handler import DBHandler

class PostService:
    def __init__(self):
        self.db_handler = DBHandler()

    def create_post(self):
        pass

    def delete_post(self):
        pass

    def get_post(self, id):
        return self.db_handler.find_item_one(condition={"id":id}, db_name="bulletinboard",collection_name="question")

    def get_post_list(self):
        return self.db_handler.find_item(db_name="bulletinboard",collection_name="question")

    def update_post(self):
        pass
