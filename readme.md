<!DOCTYPE html>
<html>
<head>
  <title>Проект "ChatBox"</title>
</head>
<body>
  <h1>Проект "ChatBox"</h1>
  <div align='center'>
    <img align="center" alt="ChatBox Logo" width="500" src="https://i.imgur.com/uTJjC0B.jpg">
  </div>
  <h2>Описание проекта</h2>
  <p>Это проект ChatBox, который представляет собой простой чат-сервер и клиентское приложение для обмена сообщениями между пользователями.</p>
  
  <h2>Требования</h2>
  <ul>
    <li>Python 3.x</li>
    <li>Библиотеки: <code>socket</code>, <code>ssl</code>, <code>sys</code>, <code>argparse</code>, <code>signal</code>, <code>threading</code>, <code>sqlalchemy</code>, <code>werkzeug</code></li>
  </ul>

  <h2>Структура проекта</h2>
  <ul>
    <li><code>client.py</code>: Модуль клиентского приложения для входа, регистрации, отправки и получения сообщений.</li>
    <li><code>server.py</code>: Модуль сервера для обработки подключений клиентов, регистрации, входа и передачи сообщений между клиентами.</li>
    <li><code>database.py</code>: Модуль базы данных для работы с базой данных, хранения информации о зарегистрированных пользователях, хэширования паролей и генерации рандомных строк для соли паролей.</li>
    <li><code>UI/</code>: Папка с файлами пользовательского интерфейса.</li>
    <li><code>TLS/</code>: Папка с файлами для поддержки безопасного соединения через протокол TLS.</li>
    <li><code>BUILDING/</code>: Папка с исходными файлами для сборки исполняемого файла.</li>
    <li><code>RELEASE/</code>: Папка с уже собранными исполняемыми файлами для ОС Linux и Windows.</li>
    <ul>
      <li><code>Client/</code>: Папка с клиентскими исполняемыми файлами.</li>
      <ul>
        <li><code>ChatBox</code>: Исполняемый файл клиентского приложения для ОС Linux.</li>
        <li><code>ChatBox.exe</code>: Исполняемый файл клиентского приложения для ОС Windows.</li>
      </ul>
      <li><code>Server/</code>: Папка с серверными исполняемыми файлами.</li>
      <ul>
        <li><code>server</code>: Исполняемый файл сервера для ОС Linux.</li>
        <li><code>server.exe</code>: Исполняемый файл сервера для ОС Windows.</li>
        <li><code>server.crt</code>: Сертификат сервера для поддержки безопасного соединения.</li>
        <li><code>server.key</code>: Ключ сервера для поддержки безопасного соединения с фразой расшифровки "sirius".</li>
      </ul>
    </ul>
  </ul>

  <h2>Установка и запуск</h2>
  <ol>
    <li>Склонируйте репозиторий с проектом:
      <pre><code>git clone https://github.com/GoldenEagle74/Chat_Project.git</code></pre>
    </li>
    <li>Перейдите в каталог проекта:
      <pre><code>cd Chat_Project</code></pre>
    </li>
    <li>Установите необходимые зависимости:
      <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li>Запустите сервер:
      <pre><code>python server.py [--host HOST] [--port PORT]</code></pre>
      или используйте исполняемый файл:
      <ul>
        <li>Для ОС Linux:
          <pre><code>./RELEASE/Server/server [--host HOST] [--port PORT]</code></pre>
        </li>
        <li>Для ОС Windows:
          <pre><code>RELEASE\Server\server.exe [--host HOST] [--port PORT]</code></pre>
        </li>
      </ul>
    </li>
    <li>Запустите клиентское приложение:
      <pre><code>python client.py [--host HOST] [--port PORT]</code></pre>
      или используйте исполняемый файл:
      <ul>
        <li>Для ОС Linux:
          <pre><code>./RELEASE/Client/ChatBox [--host HOST] [--port PORT]</code></pre>
        </li>
        <li>Для ОС Windows:
          <pre><code>RELEASE\Client\ChatBox.exe [--host HOST] [--port PORT]</code></pre>
        </li>
      </ul>
    </li>
  </ol>

  <h2>Настройка сервера</h2>
  <p>При запуске сервера вы можете указать опции <code>--host</code> и <code>--port</code>, чтобы настроить адрес и порт, на котором будет работать сервер. Если опции не указаны, сервер будет запущен на адресе по умолчанию и порту 25565.</p>

  <h2>Разработчики</h2>
  <ul>
    <li>GoldenEagle74</li>
    <li>fairygirl1</li>
  </ul>

  <h2>Лицензия</h2>
  <p>Этот проект лицензирован под лицензией MIT.</p>

  <hr>
</body>
</html>
