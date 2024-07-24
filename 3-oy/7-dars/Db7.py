import json

class Db(object):

    def get_users(self):
        try:
            file = open("../users.json", "r")
            return json.load(file)
        except:
            file = open("../users.json", "w")
            file.close()
            return []

    def save(self):
        users = self.get_users()
        users.append(self.__dict__)
        file = open("../users.json", "w")
        json.dump(users, file, indent=4)
        file.close()

    @staticmethod
    def get_user(username, password):
        users = json.load(open("../users.json", "r"))
        for user in users:
            if user["username"] == username and user["password"] == password:
                return user

        return {}
