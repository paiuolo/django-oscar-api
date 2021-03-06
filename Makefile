.PHONY: test install sandbox

install:
	pip install -e .
	pip install django-oscar-api[test]
	pip install django-oscar-api[docs]

sandbox: install
	python sandbox/manage.py migrate
	python sandbox/manage.py loaddata product productcategory productattribute productclass productattributevalue category attributeoptiongroup attributeoption stockrecord partner voucher country

test: 
	python sandbox/manage.py test oscarapi

coverage:
	coverage run sandbox/manage.py test oscarapi
	coverage report -m
	coverage xml -i

docs: install
	cd docs && make clean && make html

# patch
vanilla: install
	python vanilla/manage.py migrate
	python vanilla/manage.py loaddata auth catalogue partner

bookstore: install
	python bookstore/manage.py migrate
	python bookstore/manage.py loaddata auth catalogue partner
