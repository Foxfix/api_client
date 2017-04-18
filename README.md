# api_client
    git clone https://github.com/Foxfix/api_client.git
    cd api_client/
    pip install -r requirements.txt
    python manage.py runserver
    python manage.py migrate
    python manage.py createsuperuser

    http://127.0.0.1:8000/api/  

![api](https://goo.gl/lHXE8U)

доступно лишь админу. При выходе из админки, получим

![api](https://wmpics.pics/di-48SX.png)

    http://127.0.0.1:8090/api/register/

![api](https://wmpics.pics/di-WSHS.png)

    http://127.0.0.1:8090/api/login/
    
![api](https://wmpics.pics/di-SJJR.png)  

    http://127.0.0.1:8090/api/20/  id
    
![api](https://wmpics.pics/di-PL8U.png)

если войдем под личным аккаунтом, 
![api](https://wmpics.pics/di-D4JC.png)

Сразу после регистрации пользователь не активен, его активируют из админки
 ![api](https://wmpics.pics/di-0V5T.png)
