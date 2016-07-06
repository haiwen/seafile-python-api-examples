#!/usr/bin/env python

from seaserv import seafile_api

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

MAX_INT = 2147483647
repos_all = seafile_api.get_repo_list(0, MAX_INT)

for repo in repos_all:
    owner = seafile_api.get_repo_owner(repo.id)
    print "%s %30s %30s %10s" % (repo.id, repo.name, owner, sizeof_fmt(repo.size))
