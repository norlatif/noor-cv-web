from nicegui import ui
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create database engine (using SQLite for simplicity)
engine = create_engine('sqlite:///app.db', echo=True)
Base = declarative_base()

# Define your model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

# Create tables
Base.metadata.create_all(engine)

# Create session factory
Session = sessionmaker(bind=engine)

def get_all_users():
    session = Session()
    users = session.query(User).all()
    return [{'id': user.id, 'name': user.name} for user in session.query(User)]

def refresh_table():
    users_table.rows = get_all_users()
    ui.notify('Table refreshed!')

def button_clicked():
    session = Session()
    new_user = User(name='Test User')
    session.add(new_user)
    session.commit()
    refresh_table()
    ui.notify('User added to database!')

ui.label('Hello World').classes('text-h3')
ui.button('Click me!', on_click=button_clicked)

# Add table to display users
columns = [
    {'name': 'id', 'label': 'ID', 'field': 'id'},
    {'name': 'name', 'label': 'Name', 'field': 'name'},
]
users_table = ui.table(columns=columns, rows=get_all_users()).classes('w-full')
ui.button('Refresh Table', on_click=refresh_table)

ui.run(reload=True)
