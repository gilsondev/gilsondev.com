# -*- coding: utf-8 -*-

from __future__ import with_statement

from fabric.api import *
from fabric.colors import red
from fabric.contrib.files import exists

from contextlib import contextmanager as _contextmanager

# TODO: Refatorar script para:
#
#   1 - Rodar script shell para atualizar sistema e pacotes básicos:
#       - python-dev;
#       - python-setuptools;
#       - python-software-properties;
#       - git;
#       - postgresql-server-9.1-dev;
#       - postgresql-9.1;
#       - nginx;
#
#   2 - Instalar pacotes python básicos:
#       - virtualenv;
#       - virtualenvwrapper;
#       - pip;
#
#   3 - Fazer checkout do projeto ou atualizar;
#   4 - Criar ambiente virtualizado;
#   5 - Instalar requirements.txt;
#   6 - Sincronizar e executar migrações;
#   7 - Coletar arquivos estáticos;
#   8 - Criar link simbólico do nginx.conf;
#   9 - Reiniciar nginx;
#   10 - Iniciar gunicorn.
#
#


env.hosts = ['gilsondev.com']
env.user = 'gilsondev'
env.project = 'gilsondev'
env.virtualenv_project = '/home/%s/%s' % (env.user, env.project)
env.repository = 'git://github.com/gilsondev/gilsondev.com.git'


def apt_get(*packages):
    """Structure for apt-get"""
    sudo('apt-get -y --no-upgrade install %s' % ' '.join(packages), shell=False)


def pip(*packages):
    """Structure for install python packages in the PyPi"""
    run('pip install %s' % ' '.join(packages), shell=False)


def is_installed(package):
    """Verify if package is installed"""
    with settings(hide('warnings', 'stderr'), warn_only=True):
        result = sudo('dpkg -s %s' % package)
    if result.failed is False:
        return True
    return False


@_contextmanager
def virtualenv():
    """Activate virtualenv"""
    with cd(env.virtualenv_project):
        with prefix('source ./bin/activate'):
            yield


def update():
    """Update packages"""
    print('Updating system...')
    sudo('apt-get update', shell=False)
    sudo('apt-get upgrade', shell=False)
    return


def install_git():
    """Install Git"""
    if is_installed('git'):
        warn(red('git is already installed', bold=True))
    else:
        apt_get('git')
    return


def install_postgresql():
    """Installing PostgreSQL Server"""
    if is_installed('postgresql-server-dev-9.1'):
        warn(red('postgresql-server-dev is already installed', bold=True))
    else:
        apt_get('postgresql-server-dev-9.1')

    if is_installed('postgresql-9.1'):
        warn(red('postgresql is already installed', bold=True))
    else:
        apt_get('postgresql-9.1')
    return


def install_nginx():
    """Install Nginx package in apt-get"""

    # Installing python-software-properties
    if is_installed('python-software-properties'):
        warn(red('python-software-properties is already installed', bold=True))
    else:
        apt_get('python-software-properties')

    # Installing Nginx

    if is_installed('nginx'):
        warn(red('Nginx is already installed', bold=True))
    else:
        sudo('add-apt-repository ppa:nginx/stable')
        sudo('apt-get update')
        apt_get('nginx')
    return


def install_python_packages():
    """Install Python Packages"""

    # Install python-dev
    if is_installed('python-dev'):
        warn(red('python-dev is already installed', bold=True))
    else:
        apt_get('python-dev')

    # Install python-setuptools
    if is_installed('python-setuptools'):
        warn(red('python-setuptools is already installed', bold=True))
    else:
        apt_get('python-setuptools')

    # TODO: Verify package installed
    # Install virtualenv and pip
    sudo('easy_install virtualenv pip')


def prepare_virtualenv():
    """Prepare virtualenv project"""
    run('virtualenv --no-site-packages --unzip-setuptools %s' % env.project)


def checkout_project():
    """Checkout or update project source code"""
    if exists('/home/%s/%s' % (env.user, env.project)):
        with lcd('/home/%s/%s' % (env.user, env.project)):
            run('git pull')
    else:
        with lcd('/home/%s' % env.user):
            run('git clone %s %s' % (env.repository, env.project))


def install_requirements():
    """Install all dependencies of the project"""
    with virtualenv():
        run('pip install -r requirements.txt')


def deploy():
    update()
    install_git()
    install_nginx()
    install_postgresql()
    install_python_packages()
    checkout_project()
    prepare_virtualenv()
    install_requirements()
