
import gzip, glob
for fname in glob.glob("*.edf"):
    data = open(fname, "rb").read()
    with gzip.GzipFile(fname+".gz",mode="wb",compresslevel=4) as g:
        g.write( data )
    print("Done",fname, end="\r")
    os.remove(fname)
    