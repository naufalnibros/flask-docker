from flask import Flask, render_template, request, redirect, url_for, jsonify, send_file, session
import sqlite3 as lite
from peewee import *
import os, time, datetime, random, requests, werkzeug, uuid
from werkzeug.utils import secure_filename
from random import randint
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)
app.secret_key="#KJH*&KJH"

app.config['UPLOAD_DIR'] = 'static/gambar/'
app.config['ALLOWED_EXTENSIONS'] = set(['png','jpg','jpeg'])

@app.route('/')
def index():
    dt= str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    return render_template('index.html', dt=dt)

if __name__ == 'src':
    app.debug = True
       