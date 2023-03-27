from models.entities.User import User

class ModelUser():

    @classmethod
    def login(cls, db, user):
        try:
            cursor = db.connect.cursor()
            sql = """SELECT id, correo, password FROM usuarios
                    WHERE correo='{}'""".format(user.correo)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                user=User(row[0],row[1],User.check_password(row[2],user.password))
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(cls, db, id):
        try:
            cursor = db.connect.cursor()
            sql="SELECT id, correo FROM usuarios WHERE id={}".format(id)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                return User(row[0],row[1],None,)
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
