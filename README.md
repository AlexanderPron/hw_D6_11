# library
Для запуска и проверки приложения:
1) Скопируйте репозиторй: "git clone https://github.com/AlexanderPron/hw_D6_11.git"
2) Создайте новую виртуальную среду окружения: "virtualenv library"
3) Перейдите в каталог с проектом: "cd library"
4) Активируйте виртуальную среду:  ". ./Scripts/activate" или "source ./Scripts/activate"
5) Установите необходимые зависимости: "pip install -r requirements.txt"
6) Перейдите далее в каталог с приложением: "cd library" (Вы должны оказать на одном уровне с файлом manage.py)
7) Сделайте миграции: 
  a) "python manage.py makemigrations"
  b) "python manage.py migrate"
8) Импортируйте в бд данные из файла data.xml: "python manage.py loaddata data.xml" 
9) Запустите приложение: "python manage.py runserver"
10) В браузере перейдите по адресу: "http://127.0.0.1:8000/"
11) Проверьте работу

Учетные данные администратора:
login: admin
pass: skillfactory

Функционал:
1) Обзор всех книг в библиотеке в виде таблицы (главная страница /)
2) Обзор всех книг в библиотеке, сгруппированных по издательствам и выводом информации о книге с её изображением, если оно имеется (ссылка "Список книг" или http://127.0.0.1:8000/ph/)
3) Список всех книг, переданных в пользование с указанием подробной информации (кому, когда отдана и место проживания того, кому передана книга) (ссылка "Учёт" или http://127.0.0.1:8000/bk/)
4) Админ-панель стандартная, измененная с помощью скина Grappelli (https://django-grappelli.readthedocs.io/en/latest/)

Добавить картинку для книги можно как из админки, так и кликнув кнопку "Добавить новую книгу" на главной странице
