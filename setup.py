from setuptools import setup, find_packages

setup(
    name='SSHShark',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'paramiko',
        'cryptography',
        'tqdm',
        'flask',
    ],
    entry_points={
        'console_scripts': [
            'sshsk=sshshark:main',
        ],
    },
) 