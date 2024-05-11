import pymysql
from pymysql.connections import Connection


class DataBase:

    @staticmethod
    def connect() -> Connection:
        connection: Connection = pymysql.connect(
            user="root", passwd="root", host="localhost", database='numerolog_bot', port=3306, autocommit=True)
        return connection


    def registartion_user(self, user_id: int):
        quary = f"INSERT INTO Users (id) VALUES ({user_id});"
        with self.connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(quary)


    def check_if_user_exist(self, user_id: int):
        quary = f"SELECT id FROM Users WHERE id = {user_id} LIMIT 1;"
        with self.connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(quary)
                user = cursor.fetchone()
        return bool(user)

    def get_users_2h_autosending(self):
        query = "SELECT id FROM Users WHERE got_2h IS NULL AND TIMESTAMPDIFF(HOUR, registration_date, NOW())>=2 AND registration_date>'2023-12-06 16:00:00';"
        with self.connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                users = cursor.fetchall()
        return [int(user_id[0]) for user_id in users]


    def get_users_24h_autosending(self):
        query = "SELECT id FROM Users WHERE got_24h IS NULL AND TIMESTAMPDIFF(HOUR, registration_date, NOW())>=24 AND registration_date>'2023-12-06 16:00:00';"
        with self.connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                users = cursor.fetchall()
        return [int(user_id[0]) for user_id in users]


    def get_users_48h_autosending(self):
        query = "SELECT id FROM Users WHERE got_48h IS NULL AND TIMESTAMPDIFF(HOUR, registration_date, NOW())>=48 AND registration_date>'2023-12-06 16:00:00';"
        with self.connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                users = cursor.fetchall()
        return [int(user_id[0]) for user_id in users]


    def get_users_72h_autosending(self):
        query = "SELECT id FROM Users WHERE got_72h IS NULL AND TIMESTAMPDIFF(HOUR, registration_date, NOW())>=72 AND registration_date>'2023-12-06 16:00:00';"
        with self.connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                users = cursor.fetchall()
        return [int(user_id[0]) for user_id in users]

    def mark_got_2h_autosending(self, user_id):
        query = f"UPDATE Users SET got_2h=NOW() WHERE id={user_id} LIMIT 1;"
        with self.connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)


    def mark_got_24h_autosending(self, user_id):
        query = f"UPDATE Users SET got_24h=NOW() WHERE id={user_id} LIMIT 1;"
        with self.connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)


    def mark_got_48h_autosending(self, user_id):
        query = f"UPDATE Users SET got_48h=NOW() WHERE id={user_id} LIMIT 1;"
        with self.connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)


    def mark_got_72h_autosending(self, user_id):
        query = f"UPDATE Users SET got_72h=NOW() WHERE id={user_id} LIMIT 1;"
        with self.connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)

    def delete_user(self, user):
        query = f"DELETE FROM Users WHERE id={user} LIMIT 1;"
        with self.connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)



