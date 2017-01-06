dump:
	heroku run python manage.py dumpdata --format yaml beer.beer > data/beers.yaml
	heroku run python manage.py dumpdata --format yaml beer.brewery > data/brewery.yaml
	heroku run python manage.py dumpdata --format yaml beer.location > data/locations.yaml
	heroku run python manage.py dumpdata --format yaml beer.glassware > data/glasswares.yaml

load:
	python manage.py loaddata data/brewery.yaml
	python manage.py loaddata data/locations.yaml
	python manage.py loaddata data/glasswares.yaml
	python manage.py loaddata data/beers.yaml
