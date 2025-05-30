build:
	sudo docker-compose -f docker-compose.yml up -d --build

up:
	docker-compose -f docker-compose.yml up -d
	#docker-compose -f docker-compose.yml up -d --scale celery_worker=4

down:
	docker-compose -f docker-compose.yml down

down_v:
	docker-compose -f docker-compose.yml down -v

mm:
	docker exec -it personal_spy_web python manage.py makemigrations

m:
	docker exec -it personal_spy_web python manage.py migrate

dd:
	docker exec -t personal_spy_db  pg_dump -c -U personal_spy -d personal_spy > personal_spy_data_2024_12_12.sql

dr:
	cat personal_spy_data_2024_12_12.sql | sudo docker exec -i personal_spy_db psql -U personal_spy

rweb:
	docker restart personal_spy_web

ir:
	docker exec -it personal_spy_web pip install -r requirements.txt

csu:
	docker exec -it personal_spy_web python manage.py createsuperuser

lw:
	docker logs personal_spy_web -f
ln:
	docker logs pm_system_nginx -f

fixture:
	docker exec -it personal_spy_web python manage.py loaddata province
	docker exec -it personal_spy_web python manage.py loaddata districts
	docker exec -it personal_spy_web python manage.py loaddata municipality
	docker exec -it personal_spy_web python manage.py loaddata ward
	docker exec -it personal_spy_web python manage.py loaddata groups
	docker exec -it personal_spy_web python manage.py loaddata roles

run:
	python3 manage.py runserver

rmm:
	python3 manage.py makemigrations

rm:
	python3 manage.py migrate

rir:
	pip install -r requirements.txt

rcsu:
	python3 manage.py createsuperuser

cs:
	docker exec -it personal_spy_web python manage.py collectstatic --noinput

rfixer:
	python3 manage.py loaddata province
	python3 manage.py loaddata districts
	python3 manage.py loaddata municipality
shell:
	docker exec -it personal_spy_web python manage.py shell

vps_mm:
	docker exec -i personal_spy_web python manage.py makemigrations

vps_m:
	docker exec -i personal_spy_web python manage.py migrate