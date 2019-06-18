# Create some twins...
# For a cubic crystal we use 60 degree rotations along the 111 direction
#   e.g. ABCABC | CBACBA
from scipy.spatial.transform import Rotation
from numpy import radians, sqrt
x = radians( 60. ) / sqrt(3.)
print("no_grains 5")
# Randomised start
u0 = Rotation.from_rotvec( [0.02,0.03,0.04] )
for i,twinvec in enumerate([ (0,0,0),(x,x,x), (x,x,-x), (x,-x,x), (-x,x,x)]):
    u = (u0*Rotation.from_rotvec( twinvec )).as_dcm()
    print("U_grains_%d "%(i) + " ".join( [str(v) for v in u.ravel()] ) )
    print("pos_grains_%d "%(i) + " ".join( [str(v*0.2/x) for v in twinvec] ) )
    print("size_grains_%d 0.1"%(i))

