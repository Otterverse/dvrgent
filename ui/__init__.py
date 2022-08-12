from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, instance_relative_config=False)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

app.jinja_env.add_extension('jinja2.ext.do')
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

from ui import routes, models, filters
