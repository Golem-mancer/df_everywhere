try:
    import Image
except:
    from PIL import Image

import timeit
import numpy


a = numpy.random.rand(16,16,3) * 255
a_img = Image.fromarray(a.astype('uint8')).convert('RGB')

#Convert PIL image to string
print("To string only: \t%f" % min(timeit.Timer('a_img.tostring', "from __main__ import a_img").repeat(7, 1000)))

print("String hash: \t\t%f" % min(timeit.Timer('str.__hash__(a_img.tostring())', "from __main__ import a_img").repeat(7, 1000)))

print("md5: \t\t\t%f" % min(timeit.Timer('hashlib.md5(a_img.tostring()).hexdigest()', "from __main__ import a_img; import hashlib").repeat(7, 1000)))

print("sha1: \t\t\t%f" % min(timeit.Timer('hashlib.sha1(a_img.tostring()).hexdigest()', "from __main__ import a_img; import hashlib").repeat(7, 1000)))

print("hash: \t\t\t%f" % min(timeit.Timer('hash(a_img.tostring())', "from __main__ import a_img").repeat(7, 1000)))

print("murmur3 hash: \t\t%f" % min(timeit.Timer('mmh3.hash(a_img.tostring())', "from __main__ import a_img; import mmh3").repeat(7, 1000)))

print("imagehash - average: \t%f" % min(timeit.Timer('imagehash.average_hash(a_img)', "from __main__ import a_img; import imagehash").repeat(7, 1000)))

