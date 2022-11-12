import mysql.connector as connector

class DBhelper:
    def __init__(self):
        self.con = connector.connect(host='localhost',user='root',password='123456',database='flasktest')
        query = "create table if not exists user(userId int primary key,userName varchar(35),phone varchar(12))"
        cur = self.con.cursor()
        cur.execute(query)
        print("Table is Created!")
        
        # insert in table
    def insert_user(self,userid,username,phone):
        query = "insert into user(userId,userName,phone) values({},'{}','{}')".format(userid,username,phone)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User Created in Database!")
        
        # fetch all users
    def fetch_all(self):
        query = "select * from user"
        cur = self.con.cursor()
        cur.execute(query)
        res = []
        for row in cur:
            res.append(row)
            print(row)
            print("User Id:",row[0])
            print("user Name:",row[1])
            print("user phone",row[2])
            print()
            print()
        return res
        
    # fetch_one
    def fetch_one(self,id):
        query = "select * from user where userId = {}".format(id)
        # print(query)
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print(row)
            return row
        return False

    # delete user
    def delete_user(self,userId):
        query = "delete from user where userId = {}".format(userId)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Record Deleted!")

    # update user
    def update_user(self,userId,newName,newPhone):
        query = "update user set userName ='{}',phone='{}' where userId = {}".format(newName,newPhone,userId)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User is Updated!")