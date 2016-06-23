# TrueSight Pulse ETL Tool

Provides various tools to extract measurement data from a system and then uses the TrueSight Pulse REST API to send measurement data to
your account.


# Included Tools

The list of tools available can be listed by running the following:

```
$ tsp-etl -h
```

usage: tsp-etl [-h] {weather,apachelog,twitter,csv,log} ...

Tool to extract/transform/load into Pulse

positional arguments:
  {weather,apachelog,twitter,csv,log}
                        commands
    weather             Collects weather measurements from a city and optional
                        country code. (Future Release)
    apachelog           Parses apache logs for page status. (Future Release)
    twitter             Collects tweet data from Twitter (Future Release)
    csv                 Import CSV file
    log                 Collects measurements from log files (Future Release)

optional arguments:
  -h, --help            show this help message and exit
  

## Tool Usage

The follow sections provided usage on each of the tools


### CSV

You can load data from a CSV with the following format:

```
```

