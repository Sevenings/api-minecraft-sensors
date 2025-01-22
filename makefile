run:
	flask run

update_dependencies:
	pip freeze > requirements.txt

init_db:
	flask db init
	flask db migrate -m "Initial migration."
	flask db upgrade

update_db:
	flask db upgrade
