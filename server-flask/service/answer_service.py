from ..database.db_handler import DBHandler

class AnswerService:
    def __init__(self):
        self.db_handler = DBHandler()

    def create_answer(self):
        pass

    def delete_answer(self):
        pass

    def get_answer(self, id, post_id):
        return self.db_handler.find_item_one(condition={"id": id, "post_id": post_id},
                                             db_name="bulletinboard",collection_name="answer")

    def get_answer_list(self, post_id):
        return self.db_handler.find_item(condition={"post_id": post_id},
                                         db_name="bulletinboard",collection_name="answer")

    def update_answer(self):
        pass
