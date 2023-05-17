<!DOCTYPE html>
<html>
<head>
  <title>ChatBox</title>
</head>
<body>
  <h1 align="center">Чат на сокетах</h1>
  <div align='center'>
    <img align="center" alt="Coding" width="500" src="https://i.imgur.com/uTJjC0B.jpg">
  </div>

  <h2>Введение</h2>
  <p><strong>Цель проекта:</strong> Создать чат на сокетах для пересылки сообщений между клиентами и сервером на языке программирования Python.</p>
  <h3>Задачи проекта:</h3>
  <ol>
    <li>Разработать список пользователей.</li>
    <li>Пользователи должны иметь возможность общаться друг с другом через сервер.</li>
    <li>Реализовать регистрацию с базой данных.</li>
    <li>Предусмотреть авторизацию через базу данных.</li>
    <li>Создать графический интерфейс.</li>
  </ol>

  <h2>Описание проекта</h2>
  <p>Для реализации проекта необходимо использовать следующие зависимости:</p>
  <ul>
    <li>Python (версия 3.7 или выше)</li>
    <li>Библиотека socket для работы с сокетами</li>
    <li>Библиотека PyQt6 для создания графического интерфейса</li>
    <li>Библиотека sqlalchemy для работы с базой данных</li>
  </ul>
  <p>Проект состоит из следующих компонентов:</p>
  <ul>
    <li>TLS - шифрование данных, получаемых и передаваемых сервером.</li>
    <li>UI - файлы, необходимые для работы графического интерфейса.</li>
    <li>client.py - клиентское приложение чата.</li>
    <li>database.py - модуль для работы с базой данных.</li>
    <li>server.py - серверное приложение чата.</li>
  </ul>

  <h2>Установка</h2>
  <ol>
    <li>Установите Python версии 3.7 или выше на вашу систему.</li>
    <li>Установите необходимые зависимости, выполнив следующую команду:</li>
  </ol>
  <pre><code>pip install PyQt6 sqlalchemy</code></pre>

  <h2>Использование</h2>
  <ol>
    <li>Запустите сервер, выполнив следующую команду:</li>
  </ol>
  <pre><code>python server.py</code></pre>
  <ol start="2">
    <li>Запустите клиентское приложение, выполнив следующую команду:</li>
  </ol>
  <pre><code>python client.py</code></pre>

  <h2>

Вклад в проект</h2>
  <p>Если вы хотите внести свой вклад в проект, вы можете выполнить следующие действия:</p>
  <ol>
    <li>Форкните репозиторий.</li>
    <li>Создайте новую ветку: <code>git checkout -b my-new-feature</code>.</li>
    <li>Внесите необходимые изменения.</li>
    <li>Зафиксируйте изменения: <code>git commit -am 'Add some feature'</code>.</li>
    <li>Впишите свои изменения в ветку: <code>git push origin my-new-feature</code>.</li>
    <li>Создайте Pull Request.</li>
  </ol>

  <h2>Лицензия</h2>
  <p>Проект лицензирован под лицензией <a href="LICENSE">MIT</a>.</p>
</body>
</html>
