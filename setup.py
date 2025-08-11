from setuptools import setup, find_packages

if __name__ == '__main__':

    setup(
        name='pyZuoraEncodeV2',
        description='A Python library for encrypt CreditCard data for Zuora Payment Gateway',
        keywords='zuora, encrypt, creditcard, payment, gateway, zuoraencrypt, zuorapayment',
        license='MIT',
        url='https://github.com/LuiisDev21/pyZuoraEncode',
        version='1.1',
        author='LuiisDev21',
        author_email='Xetwy21@gmail.com',
        packages=find_packages(),
        # include_package_data=True,
        long_description=open('README.md', encoding='utf-8').read(),
        long_description_content_type='text/markdown',
        classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities"
        ],
        install_requires=["pycryptodome"],
        python_requires='>=3.6',
        
    )

