# backend
Backend for NLMKservice

### Настройка сервера

```
shh <пользователь>:<публичный ip> - подключение к серверу
sudo apt install python3-pip python3-venv git -y  - установка менеджера пакетов, виртуального окружения
```

### Разорачивание проекта

```
git clone <ссылка на репозиторий>
cd <название репозитория>
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

### Запуск сервера

```
sudo nano /etc/systemd/system/gunicorn.service  - создание конфигурационного файла для сервера (пример в репозитории)
sudo systemctl start gunicorn - запуск сервера
sudo systemctl enable gunicorn - добавление автозапуска
sudo systemctl status gunicorn - проверка статуса работы
```

### Настройка http-сервера

```
sudo apt install nginx -y  - установка
sudo ufw allow 'Nginx Full' - запросы HTTPS и HTTP
sudo ufw allow OpenSSH - запросы SSH
sudo ufw enable - включение файрвола
sudo nano /etc/nginx/sites-enabled/default - создание конфигурационного файла http-сервера (пример в репозитории)
sudo systemctl start nginx  - запуск http-сервера
```

