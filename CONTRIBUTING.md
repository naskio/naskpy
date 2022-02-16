# Contributing

## Setup

This project use [Poetry](https://python-poetry.org/) to manage dependencies.

### Install

```shell
poetry install
```

### Tests

```shell
poetry run python -m unittest discover
```

--------------------------------------------------------------------------------

## Documentation

Generated using sphinx and hosted by readthedocs.org

### Build the docs locally

```shell
cd ./docs 
make html
cd ../
```

To use apidoc run the following command before building the docs:

```shell
sphinx-apidoc -o ./_modules ../naskpy -f
```

### Readthedocs

Once enabled in readthedocs dashboard the docs will be built and deployed automatically on push to the main branch.

- [naskpy.readthedocs.io](https://naskpy.readthedocs.io)
- [naskpy.rtfd.io](https://naskpy.rtfd.io)

> A custom domain can be added throw the dashboard

### GitHub Actions

Alternatively, the docs can be built and deployed using GitHub Actions and GitHub Pages.

- `pwd` in the BASE_DIR
- `cd ./docs && make html && cd ..`

--------------------------------------------------------------------------------

## Release

To release a new version of the project you need to:

- Update the version in `pyproject.toml` (version format: `X.Y.Z`)
- Commit the changes and push to run `test_workflow`
- Create a new tag locally
- Push the tag to the remote (**don't push tag until the end of `test_workflow`**)

### Create release

Once the `test_workflow` is done, you can create run:

```shell
VERSION="0.1.1"; MESSAGE=""; git tag $VERSION -a -m $MESSAGE; git push origin $VERSION
```

### Cancel release

- Remove the tag from local and remote
  ```shell
  VERSION="0.1.1"; git tag --delete $VERSION; git push --delete origin $VERSION
  ```

- Delete release from GitHub
