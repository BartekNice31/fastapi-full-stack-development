from passlib.context import CryptContext

pwd_context=CryptContext(schemes=["bcrypt"])

class hasher:
    @staticmethod
    def verify_password(plain_password,hashed_password):
        return pwd_context.verify(plain_password,hashed_password)