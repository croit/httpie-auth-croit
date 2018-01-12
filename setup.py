from setuptools import setup

import httpie_croit


setup(
    name='httpie-croit',
    description=httpie_croit.__doc__.strip(),
    long_description=open('README.md').read().strip(),
    version=httpie_croit.__version__,
    author=httpie_croit.__author__,
    author_email='paul.emmerich@croit.io',
    license=httpie_croit.__licence__,
    url='https://github.com/croit/httpie-auth-croit',
    download_url='https://github.com/croit/httpie-auth-croit',
    py_modules=['httpie_croit'],
    zip_safe=False,
    entry_points={
        'httpie.plugins.auth.v1': [
            'httpie_croit = httpie_croit:CroitAuthPlugin'
        ]
    },
    install_requires=[
        'httpie>=0.9.0',
        'requests_ntlm'
    ],
)
