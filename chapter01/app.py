from flask import Flask
import click

app = Flask(__name__)


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name='Programmer'):
    return '<h1>Hello, %s!</h1>' % name


@app.cli.command()
def initdb():
    """Initialize the database."""
    click.echo('Init the db')
