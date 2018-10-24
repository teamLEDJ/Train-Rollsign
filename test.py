# coding: utf-8
import sys
import os
import time
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '../'))
#from modules import LED
from flask import Flask, render_template, request, redirect, url_for, json
#from PIL import Image, ImageDraw, ImageSequence

app = Flask(__name__)
led = None


@app.route('/')
def index():
    global led
    title = 'Welcome'
    message = 'Text Message'
    """
    if led == None:
        led = LED()
    """
    return render_template('index.html')


@app.route('/E233')
def E233():
    return render_template('E233.html')


@app.route('/tobu_10000')
def tobu_10000():
    return render_template('tobu_10000.html')


@app.route('/send', methods=['GET', 'POST'])
def setimg():
    # 送られてきたjsonを処理
    train_id = request.json["train_id"]
    type_pos = request.json["type_pos"]
    dest_pos = request.json["dest_pos"]
    overall_pos = request.json["overall_pos"]
    overall_flg = request.json["overall_flg"]

    # debug
    app.logger.debug(train_id)
    app.logger.debug(type_pos)
    app.logger.debug(dest_pos)
    app.logger.debug(overall_pos)
    app.logger.debug(overall_flg)
    return ""   # returnで何か返さないとエラー

"""
@app.route('/post',methods=['GET','POST'])
def post():
    global led
    title = 'Hello'
    if request.method == 'POST':
        name = request.form['name']
        text = name + u'さん、ようこそ'

        try:
            led.scroll_text(text)
        except AttributeError: pass

        # レンダリング
        return render_template('index.html',name=name, title=title)
    else:
        # リダイレクト
        return redirect(url_for('index'))
"""
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000, threaded=True)
