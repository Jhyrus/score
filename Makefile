# These targets are not files
.PHONY: contribute test syncdb requirements static

all: env/ var/ requirements

install: requirements static
	. env/bin/activate && python setup.py develop
	. env/bin/activate && python manage.py syncdb --migrate

static:
	mkdir -p public/static/

	. env/bin/activate && python manage.py collectstatic \
	         --clear \
	         --noinput \
	         --traceback \
	         -i django_extensions \
	         -i '*.coffee' \
	         -i '*.rb' \
	         -i '*.scss' \
	         -i '*.txt' \
	         -i '*.sass'

	find public/static/ -type f -not -name '*.gz' | xargs -I name sh -c 'gzip --best < name > name.gz'

virtualenv.py:
	wget -c https://raw.github.com/pypa/virtualenv/develop/virtualenv.py

requirements:
	. env/bin/activate && pip install -r requirements/develop.txt

env/: virtualenv.py
	virtualenv --prompt="(env)" env

var/:
	mkdir -p var/log
	mkdir -p var/cache
	mkdir -p var/run

test:
	./runtests.py tests/

clean:
	rm -r usr/var/log/*
	rm -r usr/var/cache/*
	rm -r usr/var/run/*
	rm -r public/static/

fullclean: clean
	rm -r env/
	rm -r virtualenv.py
