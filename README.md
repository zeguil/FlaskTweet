# BookFree
O BookFree é uma aplicação web voltada para o empréstimo e controle de livros dos usuários. Nele, o usuário pode:
* Cadastrar todos os livros que possui ou que deseja adquirir
* Solicitar o empréstimo de livros de outros usuários, emprestar seus próprios livros e gerenciar todos os empréstimos por categorias como: tempo, conservação, proximidade, etc.
* Ser publicamente avaliado de acordo com os empréstimos realizados, criando boa reputação



## Instalação
Para instalar e executar, siga os seguintes passos:  

1. Clone o repositório

    ```
    $ git clone git@github.com:zeguil/FlaskTweet.git
    ```
    
2. Entre no repositório

    ```
    $ cd FlaskTweet
    ```
    
3. Instale o `virtualenv`

    ```
    $ pip install virtualenv
    ```
    
4. Crie um novo `virtualenv`

    ```
    $ virtualenv venv
    ```
    
5. Execute o `virtualenv`
 
    ```
    $ . venv/Scripts/activate
    ```
    
6. Instale as dependências
    
    ```
    $ pip install -r requirements.txt
    ```

6. Realiza as *migrations* do banco de dados

    ```
    $ flask db init
    $ flask db migrate
    $ flask db upgrade
    ```
    
7. Execute o programa

    ```
    $ python run.py
    ```
    
8. Para parar a execução, basta pressionar CTRL+C
9. Para sair do `virtualenv`

    ```
    $ deactivate
    ```
    
# Apoio
Material de apoio do Flask:

* [Documentação](http://flask.pocoo.org/)
