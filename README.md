# Python
Developer on Python - Hackus

We should installer the mysql connector on MAC IOS
export PATH=/usr/local/mysql/bin:$PATH
export DYLD_LIBRARY_PATH=/usr/local/mysql/lib/
sudo pip install MySQL-python
python -c "import MySQLdb"

The next step is create data base with command on the serverMysql
create database BASE_POS;


On the file setting.py, we will must modificate the next seccion:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '8889',
        'NAME': 'BASE_POS',
        'raise_on_warnings': True,
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


the second seccion:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # v.1
    'ppos',
]

