
# Installing the FABLE python software

The most challenging part of developing python codes is to install them on other computers. 
Assuming you already a a python we suggest you make a clean space for installation 
as a new virtual (or conda) environment, see below. Now install the dependencies:

`python -m pip install numpy scipy matplotlib h5py pyopengl pyopengltk Pmw image pycifrw`

Now install the packages that are released on pypi:

`python -m pip install fabio xfab ImageD11`

Finally, install the packages that we didn't manage to upload to pypi yet:

`python -m pip install https://github.com/FABLE-3DXRD/fabian/archive/7301884.tar.gz`
`python -m pip install https://github.com/FABLE-3DXRD/PolyXSim/archive/b869d14.tar.gz`

Test it:

`fabian.py`  -> gui opens
`ImageD11_gui.py` -> gui opens

## First get a python interpreter onto your computer

### Using python.org or your system package manager

Go to https://www.python.org/ then select downloads and grab the latest python2.7 interpreter.
Python 3 should also work, but is much less tested with.

Create a "virtual environment" for the fable codes to be installed into.

#### Windows:

Use the py launcher as a shortcut for python and create a virtual enviroment named "fablepy2", then activate it.

`py -2 -m pip install --user virtualenv`
`py -2 -m virtualenv fablepy2`
`.\fablepy2\Scripts\activate`


### Using anaconda/miniconda

Download miniconda with python2.7 and 64-bits from :

https://docs.conda.io/en/latest/miniconda.html

On windows, open an anaconda command prompt. On linux or mac open a terminal and ensure the miniconda installation is on your path. Then create a new environment to install the software into:

`conda create -n reciprocs2019 -python=2.7`

"Activate" your new conda environment:

`conda activate reciprocs2019`

In the future when you want to run the codes again you need to open the command prompt or terminal and "activate" the environment again.



## Latest releases from pypi

The ImageD11, Fabio and xfab packages have slightly more up-to-date versions on pypi. You can install them using:

`pip install fabio ImageD11 xfab`

There are in the process of being tested for python3.x.

## Bleeding edge source code

Either clone the source code from github or have pip do this for you:

`pip install git+https://github.com/FABLE-3DXRD/ImageD11.git@master `


# Useful web links

Fable homepage:
    https://sourceforge.net/p/fable/wiki/Home/

Fable GitHub Pages:
    https://github.com/FABLE-3DXRD

ImageD11 online documentation:
    https://pythonhosted.org/ImageD11/index.html

Sebastien Merkel's notes:
    http://merkel.texture.rocks/RDX/index.php?n=ThreeD-XRD.ThreeD-XRD




## Troubleshoot Windows Launchers

Run regedit.exe. (Windows’ “default programs” control panel may work too, but it doesn’t always offer enough control, and it’s changed a lot in different Windows versions, making it harder to write instructions for.)

Go to HKEY_CLASSES_ROOT\.py. The Default value should read Python.File.

Go to HKEY_CLASSES_ROOT\Python.File\shell\open\command. The Default value should read "C:\WINDOWS\py.exe" "%L" %*.

