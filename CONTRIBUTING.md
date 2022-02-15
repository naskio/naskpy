# Contributing

## Docs

```shell
cd ./docs
sphinx-apidoc -o ./_modules ../naskpy -f 
make html
```

## From GitHub Actions

- `pwd` in the BASE_DIR
- `cd ./docs && make html && cd ..`

## Readthedocs

Will build automatically

- [naskpy.readthedocs.io](https://naskpy.readthedocs.io)
- [naskpy.rtfd.io](https://naskpy.rtfd.io)
- custom domain can be added