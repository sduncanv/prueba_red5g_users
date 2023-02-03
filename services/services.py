from models.models import User

class Services():
    def __init__(self, db) -> None:
        self.db = db


    def singup_user(self, data):
        result = self.db.session.query(User).filter(User.email == data['email']).first()

        if not result:
            user = User(
                fullname = data['fullname'],
                email = data['email'],
                password = data['password'],
                address = data['address'],
                phone_number = data['phone_number'],
                birth_date = data['birth_date']
            )
            self.db.session.add(user)
            self.db.session.commit()
            self.db.session.close()

            return {'message': 'Usuario registrado', 'status_code': 201}
        
        else:
            return {'message': 'Correo de usuario ya existente', 'status_code': 404}


    def login_user(self, data):
        result = self.db.session.query(User).filter(User.email == data['email'], User.password == data['password']).first()

        if result:
            return {'message': 'Sesión iniciada', 'status_code': 201}
        
        else:
            return {'message': 'Datos inválidos', 'status_code': 404}