# -*- coding: utf-8 -*-
"""
Created on Wed May 23 10:03:34 2018

@author: anjalidharmik
"""

import os,sys
from flask import Flask, render_template, request,redirect,url_for
import OCR_convertor_v2

def wrapper_call(file_name,folder_name):
    filename = file_name
    fldr_name = filename.split(".")[0]+"/"
    src_path = folder_name
    text_data = OCR_convertor_v2.OCR_converter(src_path,fldr_name,filename)
    return text_data

app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('/home/anjalidharmik/OCR_s_w/img/')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/success/<name>')
def success(name):
   return '%s' % name

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        file = request.files['image']
        f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        
        file.save(f)
        text_data = wrapper_call(f,"/home/anjalidharmik/OCR_s_w/")
        #return  "<html><body>"+text_data+"</body></html>"
        return redirect(url_for('success',name = text_data))
#    else:
#        file = request.args.get('image')
#        f = os.path.join(app.config['UPLOAD_FOLDER'], file)
#        
#        #file.save(f)
#        result = request.args.get('result')
#        text_data = wrapper_call(f,"/home/anjalidharmik/OCR_s_w/")
#        return redirect(url_for('success',name = text_data))
#        
if __name__ == '__main__':    
    app.run(debug = True)

