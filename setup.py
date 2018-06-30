from setuptools import find_packages
from setuptools import setup

package_name = 'zoro_rqt_reconfigure'

setup(
    name=package_name,
    version='0.1.0',
    packages=['',
              'zoro_rqt_reconfigure',
              'resource',
              'zoro_rqt_reconfigure/rqt_reconfigure',
              'zoro_rqt_reconfigure/rqt_reconfigure/python_qt_binding',
              'zoro_rqt_reconfigure/rqt_reconfigure/rqt_py_common',
              'zoro_rqt_reconfigure/rqt_reconfigure/rqt_console',
              'zoro_rqt_reconfigure/rqt_reconfigure/rqt_console/filters',
              'zoro_rqt_reconfigure/rqt_reconfigure/rqt_py_common/msg' ] ,
#     packages=find_packages(),
    package_dir={'zoro_rqt_reconfigure/rqt_reconfigure':'zoro_rqt_reconfigure/rqt_reconfigure'},
    package_data={'resource':['*.ui']},
#    data_files=[
#        ('resource', ['resource/editor_bool.ui']) 
#    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='xin liu',
    author_email='xin.liu@tusimple.com',
    maintainer='xin liu',
    maintainer_email='xin.liu@tusimple.com',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description=(
        'tests used for zoro test '
        'normal function test.'
    ),
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'zoro_rqt =zoro_rqt:main'
        ],
    },
)

