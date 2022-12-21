from setuptools import setup, find_packages

setup(name='server_messenger_gb_2022',
      version='0.1',
      description='Server messenger',
      author='Vladimir Musatov',
      author_email='vv_musatov@mail.ru',
      packages=find_packages(),
      install_requeres=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
