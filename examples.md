
We will use the "PolyXSim" package to generate test data to see how the indexing (etc) can be done.

## Single crystal grain of aluminium.

Before processing "real" data you should ensure your diffractometer calibration is correct and that the software basically works. You need to be able to index one single crystal before you can index multi-crystal datasets!

1. Generate the data (see https://sourceforge.net/p/fable/wiki/PolyXSim%20-%20input/)

> `PolyXSim.py -i Al.inp`

2. View the images

> `fabian.py Al_sx/Al_sx0000.edf`

3. Peak search the images

> `peaksearch.py -n Al_sx/Al_sx -f 0 -l 359 -t 1`

4. Check the peaks look OK

> `fabian.py Al_sx/Al_sx0000.edf` menu CrystTools -> Peaks -> Read Peaks -> peaks_t1.flt

5. Compute 3D scattering vectors

> `ImageD11_gui.py` menu Transformation:
 - load filtered peaks (peaks_t1.flt)
 - load parameters (Al_sx/Al_sx.par)
 - plot tth_eta
 - save g-vectors

6. Check the 3D scattering vectors look OK and index the grain

> `ImageD11_gui.py` menu Indexing:
 - load g-vectors
 - plot x/y/z
 - Assign peaks to powder rings (check terminal)
 - Edit parameters (min_pks=400, hkl_tol=0.1)
 - Generate trial orientations (check terminal)
 - Score trial orientations (check terminal)
 - save UBI matrices (view)
 - Write out indexed peaks (view)

7. Fit the grain position and orientation (in a real experiment you would need to refine the instrument geometry)

> `(fablepy2) makemap.py -p Al_sx/Al_sx.par -f peaks_t1.flt -u peaks_t1.ubi -U peaks_t1.map -t 0.1`

8. View the result
- `ubi_to_gff.py peaks_t1.map Al_sx\Al_sx.par peaks_t1.gff     `
- `plot_gff.py -i peaks_t1`

## Twin related Aluminium grains

A script `generate_S3.py` produced a series of grains with 60 degree rotations around 111 and displacements along 111. Aluminium does not usually do this but some other FCC metals can do something similar.

Everything as above up to indexing...

> `PolyXSim.py -i Al_S3.inp`

> `fabian.py Al_S3/Al_S30000.edf`

(output to different file S3.spt)
> `peaksearch.py -n Al_S3/Al_S3 -f 0 -l 359 -t 1 -o S3.spt`

> `ImageD11_gui.py` menu Transformation:
 - load filtered peaks (S3_t1.flt)
 - load parameters (Al_S3/Al_S3.par)
 - plot tth_eta
 - save g-vectors

> `ImageD11_gui.py` menu Indexing:
 - load g-vectors
 - plot x/y/z
 - edit parameters (ds_tol=0.012, hkl_tol=0.1, ring_1/2 = 1, uniqueness=0.05)
 - assign to rings, generate, score
 - 5 grains -> save UBI

 > `plot3d.py S3_t1.gve S3_t1.ubi` to view spots colored by grain

Fit the grain positions and orientations:
 > `makemap.py -p Al_sx\Al_sx.par -f s3_t1.flt -u s3_t1.ubi -U s3_t1.map -t 0.1`

Note that overlaps are NOT well handled here.

View the result:

 > `ubi_to_gff.py s3_t1.map Al_S3/Al_S3.par s3_t1.gff`
 > `plot_gff.py -i s3_t1.gff -c cubic`
 
 






