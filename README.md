# django4fun

git clone https://github.com/Git-DmR/django4fun.git

cd django4fun

python -m venv django4funVENV

source django4funVENV/bin/activate

python -m pip install --upgrade pip

pip install -r requirements.txt

cd d4f/

python manage.py makemigrations

python manage.py migrate

python mange.py createsuperuser

python manage.py runserver
