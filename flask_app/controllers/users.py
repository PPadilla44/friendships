from flask_app import app
from flask import render_template, redirect, request

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User

@app.route('/')
def redirect_friend():
    return redirect('/friendships')

@app.route('/friendships')
def index():
    return render_template("index.html",just_users=User.get_all(), all_users=User.get_user_and_friends())

@app.route('/create', methods=['POST'])
def create_friendship():
    friendships = User.get_all_friendships()
    userid = request.form['user']
    friendid = request.form['friend']

    for friend in friendships:
        if str(friend['user_id']) == userid and str(friend['friend_id']) == friendid:
            return redirect('/friendships')
    User.create_friendship(request.form)
    return redirect('/friendships')

@app.route('/add', methods=['POST'])
def add_user():
    User.add_user(request.form)
    return redirect('/friendships')