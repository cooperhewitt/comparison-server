import os
from flask import Flask, jsonify, request
import Image

import pprint

from lib.imgcmp import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	
	image_a = request.files['image_a']
	image_b = request.files['image_b']
			
	img_a = Image.open(image_a)
	img_b = Image.open(image_b)
	
	metrics = compare(img_a, img_b)

	return jsonify(stat="ok", metrics=metrics)
	
	
def compare(image_a, image_b):
	
	# stubin out here
		
	cmp = FuzzyImageCompare(image_a, image_b)
	sim = cmp.similarity()
	
	stats = cmp.compare()
	
	metrics = { "levenshtein": stats['levenshtein'] , 
				"nrmsd":stats['nrmsd'], 
				"psnr":stats['psnr'], 
				"similarity":sim  }
	
	return metrics