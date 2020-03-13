import click

from .repo import conect_to_repo, get_tags
from .version import increment

from github import GithubException

@click.command()
@click.argument("repo")
@click.argument("token")
@click.option('--version', '-v', required=True, type=click.Choice(['major','minor','patch']), help="version to increment")
@click.option('--sha', '-s', required=True, help="commit to be tagged")
@click.option('--message', '-m', default='', help="tag message")
@click.option('--apply/--no-apply', default=False, help="apply changes on server")
def cli(repo, token, version, sha, message, apply):
    print(f"Connecting to repo {repo}")

    try:
        repo = conect_to_repo(repo, token)
    except GithubException as exeption:
        print(f"ERROR: {exeption.data['message']}")
        return
    else:
        print('OK')

    tags = get_tags(repo)
    tag = 'v0.0.0'
    if len(tags) != 0:
        tag = tags[-1]

    new_tag = increment(version, tag)

    error = None
    try:
        t = repo.create_git_tag(new_tag, message, sha, 'commit')
    except GithubException as exception:
        error = f"ERROR Cannot create tag: {exception.data['message']}. Check if commit {sha} exist."

    if apply:
        repo.create_git_ref('refs/tags/{}'.format(t.tag), t.sha)
        print(f"Successfully created new tag {t.tag}")
    else:
        print(f"------- DRY RUN -------")
        if error is not None:
            print(error)
        else:
            print(f"Going to increment {version}. New tag {new_tag} will be created.")
            print(f"Run with --apply option to make changes.")

if __name__ == "__main__":
    cli()
