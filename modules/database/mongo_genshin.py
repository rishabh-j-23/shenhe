import pymongo
import os


client = pymongo.MongoClient(f"mongodb+srv://ryxke:{os.environ['MONGO_PASS']}@shenhedb.tqeaoxl.mongodb.net/?retryWrites=true&w=majority")
db = client['shenheDB']
uid_col = db['uids']


class MongoGenshin:

    def add(self, user: str, uid):
        user_data = {'user': user, 'uid': uid}
        uid_col.insert_one(user_data)

    def get_uid(self, user: str):
        user_data = uid_col.find_one({'user': user}, {'_id': 0, 'uid': 1})
        if user_data:
            return user_data['uid']
        return None

    def get_user(self, uid):
        user_data = uid_col.find_one(
            {'uid': str(uid)}, {'_id': 0, 'user': 1})
        if user_data:
            return user_data['user']
        return None
