# Installing the FABLE python software

The most challenging part of developing python codes is to install them on other computers. 
Assuming you already have a python we suggest you make a clean space for installation 
as a new virtual (or conda) environment (see below). Open a terminal and now install the dependencies:

> `python -m pip install numpy scipy matplotlib h5py pyopengl pyopengltk Pmw image pycifrw`

Note: on windows `python` is spelled `py -2`.

Now install the packages that are released on pypi:

> `python -m pip install fabio xfab ImageD11`

Finally, install the packages that we didn't manage to upload to pypi yet:

> `python -m pip install https://github.com/FABLE-3DXRD/fabian/archive/7301884.tar.gz`

> `python -m pip install https://github.com/FABLE-3DXRD/PolyXSim/archive/b869d14.tar.gz`

Test it:

> `fabian.py`  -> gui opens

> `ImageD11_gui.py` -> gui opens

## Getting a python interpreter onto your computer

### 1. Using python.org or your system package manager

Either go to https://www.python.org/ then select downloads and grab the latest python2.7 interpreter.
Python 3 should also work, but is much less tested. You can get python3 from the windows app store and most linux systems should have a python installed already.

Create a "virtual environment" for the fable codes to be installed into named fablepy2 here:

>`python -m pip install --user virtualenv`

>`python -m virtualenv fablepy2`

Note: on windows `python` is spelled `py -2`, in case you have more than one installation it tries to find the right one.

Now activate your environment:
> Windows: `.\fablepy2\Scripts\activate`

> Linux: `source ./fablepy2/Scripts/activate`

### 2. Using anaconda/miniconda

This is a semi-commercial python distribution that should make it easier to install packages. Often worth a try if you are having troubles. Download miniconda with python2.7 and 64-bits from :

https://docs.conda.io/en/latest/miniconda.html

On windows, open an anaconda command prompt. On linux open a terminal and ensure this miniconda installation is on your path. Then create a new environment to install the software into:

`conda create -n fablepy2 -python=2.7`

"Activate" your new conda environment:

`conda activate fablepy2`

In the future when you want to run the codes again you need to open the command prompt or terminal and "activate" the environment again.

You can try to get packages from the conda package manager although we usually find the pypi/pip versions are better supported when they work.

# Bleeding edge source code

Either clone the source code from github or have pip do this for you:

`pip install git+https://github.com/FABLE-3DXRD/ImageD11.git@master `

## Troubleshoot Windows Launchers

This was needed to create the tutorial:

- Run regedit.exe. 
- Go to HKEY_CLASSES_ROOT\.py. The Default value should read Python.File.
- Go to HKEY_CLASSES_ROOT\Python.File\shell\open\command. The Default value should read "C:\WINDOWS\py.exe" "%L" %*.

## Troubleshoot Path issues:

Check where your program comes from on windows: 
> `(fablepy2) C:\Users\wright\DataScratch\work>where PolyXSim.py`

`C:\Users\wright\DataScratch\fablepy2\Scripts\PolyXSim.py`
 
Check where your program comes from on Linux: 
> `(fablepy2) $ which PolyXSim.py`

`/home/wright/Documents/fablepy2/Scripts/PolyXSim.py`

## Getting help

- Send an email to fable-talk@lists.sourceforge.net
- Create a github issue ticket at http://github.com/FABLE-3DXRD



