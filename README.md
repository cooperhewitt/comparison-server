comparison-server
===

takes two images and returns a set of comparison metrics

Set up
---

There are a few dependencies to look out for. You can either install them manually, or use the commands below.

This can be installed locally on your system pretty easily using [virtualenv](https://pypi.python.org/pypi/virtualenv) and [pip](http://www.pip-installer.org/).

Just clone this repository and do the following commands:

    $ cd comparison-server ( or wherever you cloned it to )
    $ virtualenv venv --distribute
    $ source venv/bin/activate
    $ pip install -r requirements.txt

You can then run the server locally using [foreman](http://theforeman.org/) like this:

    $ foreman start

If you want to skip all that and you already have the dependencies installed on your system, just do:

    $ gunicorn comparison:app


Dependencies
---

* [Flask](http://flask.pocoo.org/)
* [PIL](http://www.pythonware.com/products/pil/)
* [gunicorn](http://gunicorn.org/)
* [python-Levenshtein](https://pypi.python.org/pypi/python-Levenshtein/)
* [libjpeg](http://libjpeg.sourceforge.net/) -- can be easily installed with [brew](http://brew.sh/)

Use
---

This server uses a handful of image processing algorithms to determines the similarity between two images. Presently you can only load files locally like so:


    $ curl -F image_a=@/path/to/image_a.jpg -F image_b=@/path/to/image_b.jpg http//0.0.0.0:5000/
	

resulting in something like this

    {
	  "metrics": {
	    "levenshtein": 24.479166666666657, 
	    "nrmsd": 98.73465815317296, 
	    "psnr": 37.955842578546836, 
	    "similarity": 61.60691240991981
	  }, 
	  "stat": "ok"
    }
	
You can also load images from the Internet like this:

    $ curl "http://0.0.0.0:5000/web?image_a=http://images.collection.cooperhewitt.org/17085_59010b99dc98804b_b.jpg&image_b=http://images.collection.cooperhewitt.org/4833_3cad9310584c0adb_b.jpg" | python -mjson.tool
    
Heroku
---

For your convenience, there is an [instance](http://comparison-server.herokuapp.com) of the comparison server running on [Heroku](http://heroku.com). If you'd like to try it out, use the following command. ( It may take a minute to spin up after the first request )

    $ curl "http://comparison-server.herokuapp.com/web?image_a=http://images.collection.cooperhewitt.org/17085_59010b99dc98804b_b.jpg&image_b=http://images.collection.cooperhewitt.org/4833_3cad9310584c0adb_b.jpg" | python -mjson.tool

Or, just click [here](http://comparison-server.herokuapp.com/web?image_a=http://images.collection.cooperhewitt.org/17085_59010b99dc98804b_b.jpg&image_b=http://images.collection.cooperhewitt.org/4833_3cad9310584c0adb_b.jpg) to see the result in your web browser.

Metrics
---

Currently the following image processing algorithms are being used:

* [Levenshtein Distance](http://en.wikipedia.org/wiki/Levenshtein_distance)
* [Normalized Root Mean Square Deviation](http://en.wikipedia.org/wiki/Root-mean-square_deviation)
* [Peak Signal to Noise Ratio](http://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio)
