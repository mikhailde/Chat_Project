<<<<<<< HEAD
 
=======
<h1 align="center">Чат на сокетах</h1>

<div align='center'>
<img align="center" alt="Coding" width="500" src="https://i.imgur.com/uTJjC0B.jpg">
</div>

<h3 align="center">Введение</h3>

**Цель проекта:** Создать чат на сокетах для пересылки сообщения между клиентами и сервером на языке программирования python.

**Задачи проекта:**
1. Разработать список пользователей.
2. Пользователи должны иметь возможность общаться друг с другом через сервер.
3. Реализовать регистрацию с базой данных.
4. Предусмотреть авторизацию через базу данных.
5. Создать графический интерфейс.


<h3 align="center">Описание проекта</h3>

Для реализации проекта необходимо использовать библиотеку socket для работы с сокетами и библиотеку PyQT6 для создания графического интерфейса.
Чат на сокетах позволяет пользователям обмениваться сообщениями в режиме реального времени. Регистрация и авторизация через базу данных хранит информацию обо всех подключенных и подключавшихся ранее пользователях.
**Структура проекта:**
- TLS - шифрование данных, получаемых и передаваемых сервером.
- UI - файлы, необходимые для работы графического интерфейса.
- client.py
- database.py
- server.py

Проект состоит из двух главных модулей - client.py и server.py. Для начала работы с чатом сначала необходимо запустить сервер, а после - клиента. Перед пользователем появляется графический интерфейс. Функционал: регистрация и авторизация. Все данные пользователей хранятся в базе данных sqlite.db, которая создается скриптом database.py с использованием библиотеки sqlalchemy.

Клиент реализован при помощи библиотек для создания графического интерфейса PyQt6 и UI, а также установленных модулей socket и ssl, которые обеспечивают работу самого чата, то есть процесс обмена сообщениями, и защиту передаваемых данных.

Сервер реализован при помощи встроенных библиотек threading и database и дополнительно установленных модулей socket и ssl, которые обеспечивают работу самого чата, то есть процесс обмена сообщениями, и защиту передаваемых данных.

При запуске проекта на сервере пользователь попадает в графическую оболочку. Есть две опции - авторизоваться или зарегистрироваться. При регистрации программа проверяет соответствие пароля и его подтверждения, далее, передав данные через сокет на сервер прогоняет пользователя по базе данных (databases). Если пользователь уже существует в базе, на графическом интерфейсе он получает сообщение "Exists", иначе - заносится в базу данных. 

В проекте реализована функция вывода на экран графического интерфейса отправленных сообщений - справа, и полученных сообщений - слева.

<h3 align="center">Выводы</h3>
<em>При написании группового чата на Python с использованием сокетов необходимо учитывать следующие моменты:<em><br>
1. Нужно использовать потоки для работы с несколькими клиентами. Каждый клиент должен быть обработан в отдельном потоке.<br>
2. Необходимо устанавливать соединение между клиентом и сервером через сокет. Для этого можно использовать библиотеку socket.<br>
3. Нужно учитывать возможные ошибки, например, потерю соединения с клиентом или некорректный ввод данных.<br>
4. В групповом чате нужно уметь отслеживать список пользователей, которые подключены к серверу, и передавать сообщения между ними.<br>
5. Необходимо обеспечить безопасность передачи сообщений между клиентами и сервером. Для этого можно использовать шифрование данных, например, с помощью библиотеки ssl.<br>
6. Необходимо реализовать возможность входа и выхода из аккаунта, а также просмотра списка подключенных клиентов.
>>>>>>> 632c2f04bea039779d1a50a4344832d803ab33ee
