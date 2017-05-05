from setuptools import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy

ext_modules = [
    Extension('ffm', ['fastFM/ffm.pyx'],
              libraries=['m', 'fastfm', 'openblas'],
              library_dirs=['fastFM/', 'fastFM-core/bin/',
                            'fastFM-core/externals/OpenBLAS/',],
              include_dirs=['fastFM/', 'fastFM-core/include/',
                            'fastFM-core/externals/CXSparse/Include/',
                            'fastFM-core/externals/OpenBLAS/',
                            numpy.get_include()]),
    Extension('ffm2', ['fastFM/ffm2.pyx'],
              libraries=['fastFMd', 'pthread', 'glog'],
              library_dirs=['fastFM2/fpic/fastFM',
                            '/home/ben/.hunter/_Base/033a6ff/1a47c45/e1266bb/Install/lib/'],              
              include_dirs=['fastFM2/fastFM/',
                            '/home/ben/.hunter/_Base/033a6ff/1a47c45/e1266bb/Install/include/eigen3/',
                            numpy.get_include()],
              #extra_objects=['fastFM2/fpic/fastFM/libfastFMd.a'],
                             #'/home/ben/.hunter/_Base/033a6ff/14d0f80/e1266bb/#Install/lib/libglog.a'],
              extra_compile_args=['-std=c++11'],
              extra_link_args=['-std=c++11'],
              language="c++")]


setup(
    name='fastFM',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules,

    packages=['fastFM'],

    package_data={'fastFM': ['fastFM/*.pxd']},

    version='0.2.9',
    url='http://ibayer.github.io/fastFM',
    author='Immanuel Bayer',
    author_email='immanuel.bayer@uni-konstanz.de',

    # Choose your license
    license='BSD',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',

        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['numpy', 'scikit-learn', 'scipy']
)
