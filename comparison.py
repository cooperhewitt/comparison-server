import os
from flask import Flask, jsonify, request
import Image

import urllib
import io
import cStringIO

import pprint

from lib.imgcmp import *

import logging

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	metrics = {}
	try:
		image_a = request.files['image_a']
		image_b = request.files['image_b']
			
		img_a = Image.open(image_a)
		img_b = Image.open(image_b)
		
		metrics = compare(img_a, img_b)
	except:
		print "You gotta let me know what images to process"
		
	return jsonify(stat="ok", metrics=metrics)
	
@app.route('/web', methods=['GET', 'POST'])
def web():
    metrics = {}
    
    try:
        url_a = request.args.get('image_a')
        url_b = request.args.get('image_b')

        data_a = urllib.urlopen(url_a)
        data_b = urllib.urlopen(url_b)

        file_a = io.BytesIO(data_a.read())
        file_b = io.BytesIO(data_b.read())

        img_a = Image.open(file_a)
        img_b = Image.open(file_b)    

        metrics = compare(img_a, img_b)
    except:
        logging.warning("Something went terribly wrong. It was probably your fault.")
     
    return jsonify(stat="ok", metrics=metrics)
       
    	
def compare(image_a, image_b):
			
	cmp = FuzzyImageCompare(image_a, image_b)
	sim = cmp.similarity()
	
	stats = cmp.compare()
	
	metrics = { "levenshtein": stats['levenshtein'] , 
				"nrmsd":stats['nrmsd'], 
				"psnr":stats['psnr'], 
				"similarity":sim  }
	
	return metrics