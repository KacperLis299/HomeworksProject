from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['WTF_CSRF_CHECK_DEFAULT'] = False
app.config['SECRET_KEY'] = "SECRET_KEY"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost/kacperlis"
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    db.init_app(app)

    from api.homeworks_api import homeworks_blueprint
    app.register_blueprint(homeworks_blueprint)
    from api.home_api import home_blueprint
    app.register_blueprint(home_blueprint)
    migrate.init_app(app, db)
    return app


if __name__ == "__main__":
    create_app().run(debug=True)
