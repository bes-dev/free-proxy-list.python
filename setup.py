"""
Copyright 2024 by Sergei Belousov

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from setuptools import setup, find_packages

readme = open('README.md').read()

VERSION = '2024.05.19.0'

requirements = [
    'requests',
    'beautifulsoup4'
]

setup(
    # Metadata
    name='free_proxy_list_client',
    version=VERSION,
    author='Sergei Belousov aka BeS',
    author_email='sergei.o.belousov@gmail.com',
    description='Simple python client to https://free-proxy-list.net/',
    long_description=readme,
    long_description_content_type='text/markdown',

    # Package info
    packages=find_packages(exclude=('*test*',)),

    #
    zip_safe=True,
    install_requires=requirements,

    # Classifiers
    classifiers=[
        'Programming Language :: Python :: 3',
    ],


    # install .json configs
    include_package_data=True
)
