from flask_script import Manager
from flask_migrate  import Migrate, MigrateCommand
from project import app, db
from project.models import User


migrate = Migrate(app, db)
manager = Manager(app)

# migrations
manager.add_command('db', MigrateCommand)


@manager.command
def create_db():
    """Creates the db tables."""
    db.create_all()


@manager.command
def drop_db():
    """Drops the db tables."""
    db.drop_all()

@manager.command
def clear_db():
    """Clear table."""
    try:
        num_rows_deleted = db.session.query(User).delete()
        db.session.commit()
    except:
        db.session.rollback()


@manager.command
def create_admin():
    """Creates the admin user."""
    db.session.add(User(email='ad@min.com', password='admin', admin=True))
    db.session.commit()


@manager.command
def create_data():
    """Creates sample data."""
    pass


if __name__ == '__main__':
    manager.run()