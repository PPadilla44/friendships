from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * from users ORDER BY users.last_name"
        results = connectToMySQL('friendship_schema').query_db(query)
        return results
    
    @classmethod
    def get_user_and_friends(cls):
        query = "SELECT * FROM users JOIN friendships ON \
        users.id = friendships.user_id JOIN users as user2 \
        ON user2.id = friendships.friend_id ORDER BY users.last_name"
        results = connectToMySQL('friendship_schema').query_db(query)
        return results
    
    @classmethod
    def create_friendship(cls,data):
        query = "INSERT INTO friendships(user_id,friend_id,created_at,updated_at) \
        VALUES (%(user)s,%(friend)s,NOW(),NOW());"
        return connectToMySQL('friendship_schema').query_db(query,data)
    
    @classmethod
    def add_user(cls,data):
        query = "INSERT INTO users(first_name,last_name,created_at,updated_at) \
        VALUES (%(first_name)s,%(last_name)s,NOW(),NOW())"
        return connectToMySQL('friendship_schema').query_db(query,data)

    @classmethod
    def get_all_friendships(cls):
        query = "SELECT * FROM friendships"
        results = connectToMySQL('friendship_schema').query_db(query)
        return results
        
