from setuptools import find_packages, setup

package_name = 'my_nodes'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    py_modules=[                                # add
        'my_nodes.service_node',
        'my_nodes.client_node'
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lyon',
    maintainer_email='wuliyanglyon@163.com',
    description='A custom service node and client node',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'service_node = my_nodes.service_node:main',        # add
            'client_node = my_nodes.client_node:main'           # add
        ],
    },
)
