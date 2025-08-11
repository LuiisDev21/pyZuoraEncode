![Image](https://companieslogo.com/img/orig/ZUO_BIG-16a6d064.png?t=1720244494)
# <p align="center">PyZouraEncode</p>
 
`pyZuoraEncode` is a Python library for encrypting card  data using RSA public keys, ideal for integrations with Zuora or other systems that require secure data transmission.


[![Python](https://img.shields.io/badge/Python-3.10.5-yellow.svg?logo=python&logoColor=white)](https://www.python.org/downloads/release/python-3105/) 
[![License](https://img.shields.io/badge/License-GPL-green.svg)](https://opensource.org/licenses/GPL)
[![PyPi](https://img.shields.io/badge/PyPi-View_Package-blue.svg?logo=python&logoColor=white)](https://pypi.org/project/pyZuoraEncode/) 
----------

## Installation

##### You can install the library using pip:

```sh
pip install -U pyZuoraEncode
```


## Usage

```python
from pyZuoraEncode import ZuoraEncrypt

# Initialize a public key 
public_key = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAld9m3u5AUMAxgbU9sPgzU3rDWVnxpKgpvJPQG5hVZULIxtdaBmRO8zD1WvzeZrj5dFsY4ohipCDS52kszz2w4Ex/p4fGkJh7+1yEp1HvSO9wx1f2p+JVIEdyTH7RtpX2RdejXurukHmZkb/++579ewXVNYMu5Ak152CqppyyaT/V1wus+s9966715Jlf1mTDLh5Lu4pugGoUnZfgIWwB7gVJJoHGJizSlIb1Mw7OQZtYAQjuaYlxXZPghAFIXLwP4XC5QSlK1/P2Rqh7OSuNbC6aNowgf5nUqqsjl8iz5Jhjja4hIqxmO20ilXdhT2y2awevWR10F8cvFkOWYB380QIDAQAB" 

zuora = ZuoraEncrypt(public_key)

# Encrypt data
Card = "4242424242424242|12|2030|025"
Card_Encrypted = zuora.encrypt(Card)

print(Card_Encrypted)
# Result: Ohyqa+uLuEKUYhfVTtGESLYLS6...
```


## Main Methods 
| Method                        | Description                                         |
|------------------------------|-----------------------------------------------------|
| ZuoraEncrypt(public_key=`None`) | Initializes the object with an optional public key.  |
| set_key(public_key)           | Sets or changes the public key.                      |
| encrypt(data)                 | Encrypts a string and returns the result in base64.  |



## Requierements ![Python Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/20px-Python-logo-notext.svg.png)

#### • Python 3.6 or higher
#### • PyCriptoDome:

```sh
pip install pycryptodome
```
