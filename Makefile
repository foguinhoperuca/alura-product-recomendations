.PHONY: clean

clean:
	@clear
	@date
	rm -rf school/fixtures/generated/*
	python3 manage.py migrate school zero
	python3 manage.py migrate school
	python3 seeds.py
	@date

test-enrollment-model-create:
	@clear
	@date
	python3 manage.py test school.tests.test_enrollments.EnrollmentModelTestCase.test_create
	@date

test-user-auth:
	@clear
	@date
	python3 manage.py test school.tests.test_authentication.AuthenticationUserTestCase
	@date

test-curl:
	@clear
	@date
	./test_endpoint.sh gen_get LOCAL school/courses/ admin:A12345678a | jq
	@date

ctags:
	@clear
	ctags --options=.ctags -R .
	ctags --options=.ctags -R -e .

dump-fixture-model:
	@clear
	@date
	@echo "" > school/fixtures/model.json
	python3 manage.py dumpdata school.course | jq > school/fixtures/model.json
	@date

