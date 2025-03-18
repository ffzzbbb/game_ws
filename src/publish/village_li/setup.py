from setuptools import find_packages, setup

package_name = 'village_li'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dyx',
    maintainer_email='dyx@todo.todo',
    description='A ROS 2 package for collecting and publishing game statistics.',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "publish_node=village_li.publish_node:main" 
        ],
    },
)
