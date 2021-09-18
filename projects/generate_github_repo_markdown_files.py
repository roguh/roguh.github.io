#!/usr/bin/env python3
import pprint
import sys

import requests
import yaml

MARKDOWN_TEMPLATE = """---
title: {title}
date: {date}
summary: {summary}
tags: {tags}
programming_languages: {programming_languages}
categories: {categories}
---

{body}
"""

GITHUB_LINK_TEMPLATE = '[github.com/{0}/{1}](https://github.com/{0}/{1})'

total_github_requests = 0

# parse YAML dates as strings
NoDatesSafeLoader = yaml.SafeLoader
NoDatesSafeLoader.yaml_implicit_resolvers = {
    k: [r for r in v if r[0] != 'tag:yaml.org,2002:timestamp'] for
        k, v in NoDatesSafeLoader.yaml_implicit_resolvers.items()
}


def markdown_link(link):
    """Format a URL as a markdown URL."""
    return '[{}]({})'.format(link, link)


def github(route=None, url=None):
    global total_github_requests
    """Make a request to the GitHub API."""
    r = requests.get('https://api.github.com/' + route if url is None else url,
                     headers={'Accept': 'application/vnd.github.v3+json'})
    if r.status_code > 299:
        raise Exception(route, url, r)
    total_github_requests += 1
    j = r.json()
    if type(j) is dict and j.get('message', False):
        raise Exception('{} {}\n{}\n{}'.format(route, url, j.get('message'), j.get('documentation_url')))
    return j


def md_contents(username, project, repo=None, metadata=None):
    """Convert a given GitHub users' project into a markdown string.

    Makes requests to the GitHub API.
    """

    if repo is None:
        repo = github('repos/{}/{}'.format(username, project))
    if metadata is None:
        metadata = dict()
    date = metadata.get('date', repo['pushed_at'])
    tags = metadata.get('tags', [])
    programming_languages = metadata.get('programming_languages', None)

    def get_languages(url):
        langues = github(url=url)
        return list(langues.keys())

    if metadata.get('useGithubLanguages', True) and programming_languages is None:
        programming_languages = get_languages(repo['languages_url'])
    else:
        programming_languages = []
    tags = tags + programming_languages
    categories = metadata.get('categories', [])
    homepage = repo['homepage']
    body_contents = 'See ' + GITHUB_LINK_TEMPLATE.format(username, project)
    print('processed', project, date, homepage, tags)
    if homepage is not None and len(homepage) > 0:
        body_contents += '\n\n' + markdown_link(homepage)
    content = MARKDOWN_TEMPLATE.format(
        summary=repo['description'],
        title=project,
        date=date,
        tags=tags,
        programming_languages=programming_languages,
        categories=categories,
        body=body_contents
    )
    return content


def md_content_for_all_repos(username, desired_repos, path='', project_count=200):
    """Fetch a user's GitHub repos, convert to markdown, and write markdown
    files to given path.
    """
    global total_github_requests

    repos = github('users/{}/repos?per_page={}'.format(username, project_count))
    skipped = list()
    done = set()

    for repo in repos:
        project_name = repo['name']
        if project_name in desired_repos:
            metadata = desired_repos[project_name] if type(desired_repos) is dict else None
            with open(path + project_name + '.md', 'w') as f:
                f.write(md_contents(username, project_name, repo,
                                    metadata=metadata))
                done.add(project_name)
        else:
            skipped.append(project_name)
    missing = set(desired_repos) - done

    if len(missing):
        print('failed to process', *list(missing))
    print('total github requests', total_github_requests)
    if len(skipped) > 0:
        print('skipped:')
        print('\n'.join(skipped))


def parse_config(filename):
    """Parse a YAML config file."""
    try:
        with open(filename) as f:
            return yaml.load(f.read(), Loader=NoDatesSafeLoader)
    except Exception as e:
        print(e)
        return {}


if __name__ == '__main__':
    if len(sys.argv) > 2:
        print('generating markdown for', *sys.argv[1:])
        print(md_content_for_all_repos(*sys.argv[1:]))
    elif len(sys.argv) == 2:
        print('generating markdown for', *sys.argv[1:])
        md_content_for_all_repos(sys.argv[1], parse_config('repo_list.yaml'))
    else:
        print('USAGE: {} username [repo_name [repo_name...]]')
        print('Using config:')
        pprint.pprint(parse_config('repo_list.yaml'))
