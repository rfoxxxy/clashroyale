import json
import urllib.request
from setuptools import setup, find_packages

with open('README.md', encoding='utf8') as f:
    long_description = f.read()

setup(
    name='clashroyale',
    packages=find_packages(),
    version='4.0.1',
    description='An (a)sync wrapper for royaleapi.com',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    license='MIT',
    keywords=['clashroyale', 'wrapper', 'cr', 'royaleapi'],
    include_package_data=True,
    install_requires=['aiohttp', 'python-box', 'requests', 'async_generator'],
    python_requires='>=3.5',
    project_urls={
        'Source Code': 'https://github.com/cgrok/clashroyale',
        'Issue Tracker': 'https://github.com/cgrok/clashroyale/issues',
        'Documentation': 'https://clashroyale.readthedocs.io/',
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Games/Entertainment :: Real Time Strategy',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Natural Language :: English'
    ]
)

# Reload Constants #
try:
    data = json.loads(urllib.request.urlopen('https://fourjr-webserver.herokuapp.com/cr/constants').read())
except (TypeError, urllib.error.HTTPError, urllib.error.URLError):
    pass
else:
    if data:
        del data['info']
        with open('clashroyale/constants.json', 'w') as f:
            json.dump(data, f)
