
# coding: utf-8

# In[18]:


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

import pymysql
# this will allow model classes to be shared across otehr classes(accessible)
Base = declarative_base()


# In[19]:


class Users(Base):
    __tablename__ = "users"
    
    id = Column('idusers',Integer, primary_key=True)
    email = Column('email', String(45), unique=True)
    password = Column('password', String(45))

    def __init__(self, id, email, password):
        self.id = id
        self.email = email
        self.password = password
        
    
    # check if user exists
    def is_user(_email,_password):
        # create session
        session = Session()
        # query session
        users = session.query(Users).filter_by(email=_email,password=_password).all()
        count = len(users)
        # close session
        session.close()
        if count > 0:
            return True
        
        return False
    
    # add user to database (signup)
    def add_user(_email,_password):
        # create session
        session = Session()
        # create user
        user = Users(id = 0,email=_email,password=_password)
        # add to session
        session.add(user)
        # commit session
        session.commit()
        # close session
        session.close()


# In[20]:


class ToDoList(Base):
    __tablename__ = "todolist"
    
    id = Column('idusers',Integer, primary_key=True)
    title = Column('title',String(45),primary_key=True)
    description = Column('description', String(200))
    
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description
    
    #add task to the database    
    def add_todo(_title,_description):
        #create Session
        session = Session()
        #create object of ToDoList
        task = ToDoList(id=1,title=_title,description=_description)
        # add to session
        session.add(task)
        #commit the session
        session.commit()
        #close the session
        session.close()
        return True
    
    
    def get_tasks():
        session = Session()
        # query session
        tasks = session.query(ToDoList).all()
        return tasks
#         session.close()

    
    def delete_all():
        session = Session()
        session.query(ToDoList).delete()
        session.commit()
        session.close()
        return True
        
    


# In[21]:


engine = create_engine("mysql+pymysql://root:root@localhost/flaskapp")
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)


# In[22]:




