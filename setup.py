from setuptools import find_packages, setup

setup(
    name='netbox-role-custom-fields',
    version='0.1.1',
    description='Plugin for unique "custom" fields in Netbox',
    url='',
    author='Bastian Leicht <bl@city-pc.de>',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
)
