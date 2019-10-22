from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
# import Cython.Compiler.Options
# Cython.Compiler.Options.annotate = True

setup(ext_modules=[Extension("cython_with_c",
                             sources=["cython_with_c.pyx"],
                             language="c")],
      cmdclass={'build_ext': build_ext})
