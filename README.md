comparison-server
===

takes two images and returns a set of comparison metrics

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
	
metrics
---

* [Levenshtein Distance](http://en.wikipedia.org/wiki/Levenshtein_distance)
* [Normalized Root Mean Square Deviation](http://en.wikipedia.org/wiki/Root-mean-square_deviation)
* [Peak Signal to Noise Ratio](http://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio)


dependancies
---

* PIL
* python-Levenshtein
