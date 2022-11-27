import pymongo
import os


# client = pymongo.MongoClient(os.environ['MONGO_KEY'])
client = pymongo.MongoClient(
    f"mongodb+srv://Ryxke:{os.environ['MONGO_PASS']}@shenhedb.tqeaoxl.mongodb.net/?retryWrites=true&w=majority")
db = client['shenheDB']
uid_col = db['uids']


class MongoGenshin:

    def add(self, user: str, uid):
        uids = {'user': f'{user}', 'uid': f'{uid}'}
        uid_col.insert_one(uids)

    def get_uid(self, user: str):
        u = []
        for x in uid_col.find({}, {"_id": 0, "user": 1, "uid": 1}):
            u.append(x)

        for i in range(len(u)):
            if u[i]['user'] == user:
                uid = u[i]['uid']

                return int(uid)

    def get_user(self, uid):
        u = []
        for x in uid_col.find({}, {"_id": 0, "user": 1, "uid": 1}):
            u.append(x)

        for i in range(len(u)):
            if u[i]['uid'] == str(uid):
                user = u[i]['user']

                return str(user)
