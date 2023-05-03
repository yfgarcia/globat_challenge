from flask import Flask, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER


# Creating the engine to connnect with ElephantSQL
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
#Base.metadata.create_all(engine)

# Create a session factory to manage the pool connections
Session = sessionmaker(bind=engine)

# Create the flaskk app
app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)
