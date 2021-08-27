export SECRET_KEY='casey12'


export MAIL_USERNAME='musilacasey@gmail.com'
export MAIL_PASSWORD='musila'
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python3 manage.py server --port 4300