from setuptools import setup

descripcion_longa = open('Readme.txt').read()
setup(
    name="Exemplo de empaquetado",
    version="0.12",
    description="Descripcion breve do Exemplo empaquetado",
    long_description=descripcion_longa,
    keywords="empaquetado instalador paquetes",
    packages=[]
)
