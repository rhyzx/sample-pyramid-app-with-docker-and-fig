# README

## Getting Started

- install docker(1.3) and fig
- `fig up`
- visit http://your-virtualmachine-ip:6543/foos to see basic CRUD


## Tips

- `fig build` to update container after changed `requirements.txt` or `Dockerfile`
- `fig rm` to clear database


# LOG
* pyramid does not support nested form `<input name="item[name]">`
* alchemy does not support massive assign? `Foo(dict)`
