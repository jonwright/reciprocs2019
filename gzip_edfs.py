from __future__ import print_function
import gzip, glob, os
for fname in glob.glob("*.edf"):
    data = open(fname, "rb").read()
    with gzip.GzipFile(fname+".gz",mode="wb",compresslevel=4) as g:
        g.write( data )
    print("Done",fname, end="\r")
    os.remove(fname)
    