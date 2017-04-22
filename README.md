# api_client
    git clone https://github.com/Foxfix/api_client.git
    cd api_client/
    pip install -r requirements.txt
    python manage.py runserver
    python manage.py migrate
    python manage.py createsuperuser

    http://127.0.0.1:8000/api/  

![api](https://goo.gl/lHXE8U)

    http://127.0.0.1:8090/api/register/

![api](https://wmpics.pics/di-WSHS.png)

    http://127.0.0.1:8090/api/login/
    
![api](https://wmpics.pics/di-SJJR.png)  

    http://127.0.0.1:8090/api/20/  id
    
если войдем под личным аккаунтом, можем изменять определенные данные профиля.
![api](http://ipic.su/img/img7/fs/scrin.1492894317.png) 

Сразу после регистрации пользователь не активен, его активируют из админки
 ![api](https://wmpics.pics/di-0V5T.png)


    Для доп. проверки

    http://127.0.0.1:8090/login/

    http://127.0.0.1:8090/register/

    http://127.0.0.1:8090/logout/
    
    При создании по умолчанию пользователь не активен, is_active=False. 
    
    Но accaunt = Open. Пользователь может сменить на accaunt = Close, закрыв его. 
    
    После закрытия пользователем аккаунта, админ может удалять его.
    
    ![api](http://ipic.su/img/img7/fs/close.1492894356.png)
    
    
![api](https://wmpics.pics/di-YOUD.png) 
