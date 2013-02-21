"""
    Script for building the example.
    
    Usage:
    python setup.py py2app
    """
from distutils.core import setup
import py2app

plist = dict(NSMainNibFile="MainMenu")
setup(
      name="LearningPyObjc",
      app=["main.py"],
      data_files=["MainMenu.nib", "CompareWindow.nib"],
      options=dict(py2app=dict(plist=plist)),
      )