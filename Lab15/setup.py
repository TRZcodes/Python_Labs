from distutils.core import setup, Extension
setup(name='mod', version='1.0', ext_modules=[Extension('mod', sources=['lab15/mod.c','lab15/euclidean.c','lab15/insertion.c'])])
