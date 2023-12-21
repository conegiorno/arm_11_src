from setuptools import find_packages, setup

package_name = 'maze_goal'

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
    maintainer='Konrad Jędrzejewski',
    maintainer_email='konrad.jedrzejewski@student.put.poznan.pl',
    description='Package for ARM_11 laboratory',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'maze_goal = maze_goal.subscriber_member_function:main',
        ],
    },
)
