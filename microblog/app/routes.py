import io
import os
import random
import numpy
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.axes import Subplot
from PIL import Image

from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from app import zigzag
from app.zigzag import *
from app import image2RLE
from app import RLE2image
from app import *

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    tam1 = { 'size': os.path.getsize("uncompressed.jpg")}
    tam2 = { 'size': os.path.getsize("compressed_image.jpg")}
    return render_template('index.html', title='Instituo Politécnico Nacional', user=user, posts=posts, tam1=tam1, tam2=tam2)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title= 'Sing in', form=form)

@app.route('/image2RLE')
def image2RLE():
    return dict(principal="image2RLE.py")

@app.route('/RLE2image')
def RLE2image():
    return dict(compresion="RLE2image.py")

@app.route('/uncompressed.jpg')
def uncompressed():
    img = Image.open('uncompressed.jpg')
    fig = plt.figure()
    ax = Subplot(fig,111)
    ax.imshow(img, cmap="gray")
    fig.add_subplot(ax)

    output = io.BytesIO()
    FigureCanvas(fig).print_jpg(output)
    return Response(output.getvalue(), mimetype='image/jpg')

@app.route('/compressed_image.jpg')
def compressed_image():
    img = Image.open('compressed_image.jpg')
    fig = plt.figure()
    ax = Subplot(fig,111)
    ax.imshow(img, cmap="gray")
    fig.add_subplot(ax)

    output = io.BytesIO()
    FigureCanvas(fig).print_jpg(output)
    return Response(output.getvalue(), mimetype='image/jpg')


