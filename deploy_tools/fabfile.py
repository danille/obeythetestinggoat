from fabric.contrib.files import append, exists, sed
from fabric.api import cd, env, local, run
import random

REPO_URL = 'https://github.com/danille/testing_goat.git'


def deploy():
    site_folder = f'/home/{env.user}/sites/{env.host}/source'
    run(f'mkdir -p {site_folder}')
    with cd(site_folder):
        _get_latest_source()
        _update_settings(env.host)
        _update_virtualenv()
        _update_static_files()
        _update_database()


def _get_latest_source():
    if exists('.git'):
        run('git fetch')
    else:
        run(f'git clone {REPO_URL} .')
    current_commit = local('git log -n 1 --format=%H', capture=True)
    run(f'git reset --hard {current_commit}')


def _update_settings(site_name):
    settings_path = 'testing_goat/settings.py'
    sed(settings_path, 'DEBUG = True', 'DEBUG = False')
    sed(settings_path, 'ALLOWED_HOSTS =.+$', f'ALLOWED_HOSTS = ["{site_name}"]')
    secret_key_file = 'testing_goat/secret_key.py'
    if not exists(secret_key_file):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        key = ''.join(random.SystemRandom().choices(chars, k=50))
        append(secret_key_file, f'SECRET_KEY = "{key}"')
    append(settings_path, '\nfrom .secret_key import SECRET_KEY')


def _update_virtualenv():
    if not exists('../venv/bin/pip'):
        run(f'python3.6 -m venv ../venv')
    run('../venv/bin/pip install -r requirements.txt')


def _update_static_files():
    run('../venv/bin/python manage.py collectstatic --noinput')


def _update_database():
    if not exists('../database'):
        run('mkdir ../database')
    run('../venv/bin/python manage.py migrate --noinput')
