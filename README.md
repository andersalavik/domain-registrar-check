# domain-registrar-check


## Info

Script to find Registrar and Nameservers from a file with domainnames.

## How to

### Install requirements

```bash
$ python3 -m pip install -r requirements.txt
```

### Run

#### Output data in JSON format

```bash
$ python3 check.py -f domains-example.txt --json
```

#### Debug

```bash
$ python3 check.py -f domains-example.txt --json --log debug
```
