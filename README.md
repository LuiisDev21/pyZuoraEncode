# pyZuoraEncode

`pyZuoraEncode` is a Python library for encrypting data using RSA public keys, ideal for integrations with Zuora or other systems that require secure data transmission.

## Installation

You can install the library by cloning this repository and using pip:

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
Card_Encrypted = zuora.encrypt(data)

print(Card_Encrypted)
```

## Main Methods

- `ZuoraEncrypt(public_key=None)`: Initializes the object with an optional public key.
- `set_key(public_key)`: Sets or changes the public key.
- `encrypt(data)`: Encrypts a string and returns the result in base64.

## Requirements

- Python >= 3.10
- pycryptodome

## License

MIT

## Author

Taiinyy & MrXetwy21  
[Original repository](https://github.com/MrXetwy21/XetMap)

---

# pyZuoraEncode

`pyZuoraEncode` es una librería de Python que permite cifrar datos utilizando claves públicas RSA, ideal para integraciones con Zuora u otros sistemas que requieran transmisión segura de información.

## Instalación

Puedes instalar la librería clonando este repositorio y usando pip:

```sh
pip install -U pyZuoraEncode
```



## Uso

```python
from pyZuoraEncode import ZuoraEncrypt

# Inicializa una clave pública (No es la misma en todos los sitios)
public_key = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAld9m3u5AUMAxgbU9sPgzU3rDWVnxpKgpvJPQG5hVZULIxtdaBmRO8zD1WvzeZrj5dFsY4ohipCDS52kszz2w4Ex/p4fGkJh7+1yEp1HvSO9wx1f2p+JVIEdyTH7RtpX2RdejXurukHmZkb/++579ewXVNYMu5Ak152CqppyyaT/V1wus+s9966715Jlf1mTDLh5Lu4pugGoUnZfgIWwB7gVJJoHGJizSlIb1Mw7OQZtYAQjuaYlxXZPghAFIXLwP4XC5QSlK1/P2Rqh7OSuNbC6aNowgf5nUqqsjl8iz5Jhjja4hIqxmO20ilXdhT2y2awevWR10F8cvFkOWYB380QIDAQAB"  

zuora = ZuoraEncrypt(public_key)

# Encryptar la tarjeta
data = "4242424242424242|12|2030|026"
encrypted = zuora.encrypt(data)
print(encrypted)
```

## Métodos principales

- `ZuoraEncrypt(public_key=None)`: Inicializa el objeto con una clave pública opcional.
- `set_key(public_key)`: Establece o cambia la clave pública.
- `encrypt(data)`: Cifra una cadena de texto y retorna el resultado en base64.

## Requisitos

- Python >= 3.10
- pycryptodome

## Licencia

MIT

## Autor

Taiinyy & MrXetwy21  
[Repositorio original](https://github.com/MrXetwy21/pyZouraEncode)
