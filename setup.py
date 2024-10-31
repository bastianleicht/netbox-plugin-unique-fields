from setuptools import find_packages, setup

setup(
    name='netbox_role_customfields',
    version='0.1',
    description='A NetBox plugin to manage custom fields for device roles',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # Hier kannst du Abhängigkeiten eintragen, falls das Plugin welche benötigt
    ],
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
