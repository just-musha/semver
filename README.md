semver
========

CLI tool for git semantic versioning

## Usage

First you will want to create [Github access token](https://github.com/settings/tokens).

```
Usage: semver [OPTIONS] REPO TOKEN

Options:
  -v, --version [major|minor|patch]
                                  Version to increment  [required]
  -s, --sha TEXT                  Commit to be tagged  [required]
  -m, --message TEXT              Tag message
  --apply / --no-apply            Apply changes on server
  --help                          Show this message and exit.
```

Example:

```
$ semver <GITHUB_NICK>/<REPO> <TOKEN> -v minor --sha <SHA_COMMIT>
```
Apply changes:
```
$ semver <GITHUB_NICK>/<REPO> <TOKEN> -v minor --sha <SHA_COMMIT> --apply
```

## Installation From Source

To install the package after you've cloned the repository, you'll want to run the following command from within the project directory:

```
$ pip install --user -e .
```

## Preparing for Development

Follow these steps to start developing with this project:

1. Ensure `pip` and `pipenv` are installed
2. Clone repository: `git clone git@github.com:mbulatova/semver`
3. `cd` into the repository
4. Activate virtualenv: `pipenv shell`
5. Install dependencies: `pipenv install`
