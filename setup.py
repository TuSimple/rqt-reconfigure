from setuptools import find_packages
from setuptools import setup

package_name = 'rqt_reconfigure'

setup(
    name=package_name,
    version='0.4.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/' + package_name, ['package.xml']),
        ('share/rqt_resource',
               ["rqt_resource/editor_bool.ui", 
                "rqt_resource/editor_enum.ui", 
                "rqt_resource/editor_number.ui",
                "rqt_resource/editor_string.ui",
                "rqt_resource/node_selector.ui",
                "rqt_resource/paramedit_pane.ui", 
                "rqt_resource/param_main.ui",  
                "rqt_resource/param_timeline.ui",
                "rqt_resource/singlenode_parameditor.ui",
                "rqt_resource/text_filter_widget.ui"] ),
    ],
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
        'dynamic reconfigure used for zoro  '
        'normal function.'
    ),
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'rqt_gui =rqt_reconfigure.param_widget:main',
        ],
    },
)
