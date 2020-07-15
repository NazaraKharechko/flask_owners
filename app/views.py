from flask import redirect, url_for
from .db import owners
from app import app


@app.route('/')
def show_all():
    if owners:
        return redirect(url_for('owner.show_all'))
    return redirect(url_for('owner.register'))
