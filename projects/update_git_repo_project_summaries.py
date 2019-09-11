#!/usr/bin/env python3
import sys

import requests

MARKDOWN_TEMPLATE = """---
title: {title}
date: {date}
summary: {summary}
---

{body}
"""

GITHUB_LINK_TEMPLATE = '[github.com/{0}/{0}](https://github.com/{0}/{1})'


def markdown_link(link):
    return '[{}]({})'.format(link, link)


# get a list of given user's projects
def github(route):
    r = requests.get('https://api.github.com/' + route,
                     headers={'Accept': 'application/vnd.github.v3+json'})
    return r.json()


def md_contents(username, project, repo=None):
    if repo is None:
        repo = github('repos/{}/{}'.format(username, project))
        print('fetched', username, project, repo)
    date = repo['pushed_at']
    homepage = repo['homepage']
    body_contents = GITHUB_LINK_TEMPLATE.format(username, project)
    if homepage is not None and len(homepage) > 0:
        body_contents += '\n\n' + markdown_link(homepage)
    content = MARKDOWN_TEMPLATE.format(
        summary=repo['description'],
        title=project,
        date=date,
        body=body_contents
    )
    return content


def md_content_for_all_repos(username, *desired_repos):
    repos = github('users/{}/repos'.format(username))
    done = set()
    print('found {} repos for user {}'.format(len(repos), username))
    for repo in repos:
        if repo in desired_repos:
            project_name = repo['name']
            print(md_contents(username, project_name, repo))
            done.add(repo)
    return set(desired_repos) - done


if __name__ == '__main__':
    if len(sys.argv) == 3:
        print('generating markdown for', *sys.argv[1:])
        print(md_contents(*sys.argv[1:]))
    elif len(sys.argv) > 3:
        print('generating markdown for', *sys.argv[1:])
        print(md_content_for_all_repos(*sys.argv[1:]))
