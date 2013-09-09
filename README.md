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
	


dependancies
---

* PIL
* python-Levenshtein