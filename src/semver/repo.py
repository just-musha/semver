from github import Github

def conect_to_repo(repo_name, token):
    g = Github(token)
    repo = g.get_repo(repo_name)
    return repo

def get_tags(repo):
    tags = []
    for tag in repo.get_tags():
        tags.append(tag.name)
    tags.sort()
    return tags

