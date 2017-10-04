#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from app import create_app, db, models
from flask_script import Server, Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'development')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, models=models)


manager.add_command("runserver", Server(host="0.0.0.0", port=5000))
manager.add_command('shell', Shell(make_context=make_shell_context, use_ipython=True))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
