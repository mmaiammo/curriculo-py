<p align="left">
[<img src="http://www.google.com.au/images/nav_logo7.png">](http://google.com.au/)
</p>

# Como desenvolver neste app

> __Criar o ambiente virtualenv__
```
$ python3 -m venv venv
```

> __Instalar Projeto após cloná-lo do Github__
> 
> 📝 **Nota:** entre no diretório aonde o projeto foi clonado, via terminal/prompt de comando e, digite a instrução a seguir.
> 
```
$ pip install -r requirements.txt
```

>  __Dependências__: usadas até o momento
-------------------------------
```
$ pip install flask
$ pip install mypy
$ pip install flake8
$ pip install python-dotenv
$ pip install numpy
$ pip install Flask-PyMongo
$ pip install dnspython
$ pip3 install pandas --upgrade
$ pip install pymongo
$ pip install autopep8
```

> __Run freeze__: exporta todas as dependências do projeto
```
$ pip freeze > requirements.txt
```
