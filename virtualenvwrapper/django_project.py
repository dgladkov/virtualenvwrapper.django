#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2011 Doug Hellmann.  All rights reserved.
#
"""Create Django projects automatically with virtualenvwrapper.
"""

import logging
import os
import subprocess

log = logging.getLogger('virtualenvwrapper.django')


def template(_args):
    """Installs Django and runs django-admin to create a new project.
    """
    project, project_dir = args
    os.chdir(project_dir)
    subprocess.check_call(['pip', 'install', 'django'])
    call_args = ['django-admin.py', 'startroject', project]
    django_template = os.environ.get('DJANGO_DEFAULT_PROJECT_TEMPLATE')
    django_template_extensions = os.environ.get('DJANGO_DEFAULT_PROJECT_TEMPLATE_EXTENSIONS')
    if django_template:
        call_args.append('--template=%s' % django_template
    if django_template_extensions:
        call_args.append('--extenstion=%s' % django_template_extensions)
    log.info('Running "%s"', ' '.join(call_args))
    subprocess.check_call(call_args)
    return
