from flask import Flask

# print("NAME:",__name__)

app = Flask(__name__)
# app.config.get()
app.config.from_object(Config)

from app import routes  # noqa
