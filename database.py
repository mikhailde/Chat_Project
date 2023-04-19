from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, Session


engine = create_engine("sqlite:///sqlite.db", echo=True)

class Base(DeclarativeBase): pass

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)

    def __str__(self):
        return ' '.join([str(self.id),self.username,self.password])

Base.metadata.create_all(bind=engine)    

def register(username, password):
    with Session(autoflush=False, bind=engine) as db:
        user = (db.query(User).filter(User.username==username).first())
        if user: return False
        user = User(username=username, password=password)
        db.add(user)
        db.commit()
        return True
        

print(register('goldy','12345'))