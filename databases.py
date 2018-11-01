from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()



def create_product(price,quantity,color,description):
  product_object = Product(
        price=price,
        quantity=quantity,
        color=color,
        description=description)
  session.add(product_object)
  session.commit()

#create_product(7,89,'red','amazing')

pass

def update_product():
  #TODO: complete the functions (you will need to change the function's inputs)
  pass

def delete_product(their_id):
  session.query(Product).filter_by(
    id=their_id).delete()
  session.commit()

pass

def get_product(id):
  pass
