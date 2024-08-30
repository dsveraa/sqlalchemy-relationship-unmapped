from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

db_url = "sqlite:///database.db"

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# unmapped method
class BaseModel(Base):
    __abstract__ = True
    __allow_unmapped__= True 
    
    id = Column(Integer, primary_key=True)

class Address(BaseModel):
    __tablename__= "addresses"
    
    city = Column(String)
    state = Column(String)
    zip_code = Column(Integer)
    user_id = Column(ForeignKey("users.id")) # id is inherit from BaseModel in table users
    user = relationship("User", back_populates="addresses") # access user related to an address
    
    def __repr__(self):
        return f"<User(id={self.id}, city='{self.city}')"
    
class User(BaseModel):
    __tablename__ = "users"
    
    name = Column(String)
    age = Column(Integer)
    addresses = relationship(Address) # in case the class is in other file, you should use quotes ("Addresses")
    
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.name}')"
    

Base.metadata.create_all(engine)
