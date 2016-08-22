#coding: utf-8

from flask import Blueprint, request, redirect, render_template, url_for, session
import os

posts = Blueprint('posts', __name__, template_folder='templates', static_folder='static')

@posts.route('/', methods=['GET'])
def index():
	return render_template('index.html')