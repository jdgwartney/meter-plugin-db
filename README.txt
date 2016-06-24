

TRUESIGHT PULSE ETL TOOL


Provides various tools to extract measurement data from a system and
then uses the TrueSight Pulse REST API to send measurement data to your
account.



INSTALLATION


The TrueSight Pulse ETL Toll is installed via pip:

    $ pip install tspetl



AUTHENTICATION


The accompanying tool requires your login _email_ and _api token_.

These can be specified on the command line with the -e and -t command
line arguments respectively or specified by setting the following
environment variables:

-   TSP_EMAIL
-   TSP_API_TOKEN

in your shell like the following:

    export TSP_EMAIL=dude@example.com
    export TSP_API_TOKEN=api.558c71066a-0000



INCLUDED TOOLS


The list of tools available can be listed by running the following:

    $ tsp-etl -h

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


Tool Usage

The follow sections provided usage on each of the tools

CSV

The CSV (Comma Separated Value) tool allows the loading of data stored
in a file formatted as a CSV.

Usage

    usage: tsp-etl csv [-h] [-e email] [-t token] [-a hostname] [-s {api,rpc,std}]
                       [-f file_path] [-b batch_count] [-o origin] [-p id]
                       [--skip-first-line]

    optional arguments:
      -h, --help            show this help message and exit
      -e email, --e-mail email
      -t token, --api-token token
      -a hostname, --api-host hostname
      -s {api,rpc,std}, --sink-type {api,rpc,std}
      -f file_path, --file file_path
                            Path to file to import
      -b batch_count, --batch batch_count
                            How many measurements to send in each API call
      -o origin, --origin origin
                            Origin to associated with the measurements
      -p id, --application-id id
                            Application Id to associate with the measurements
      --skip-first-line     Skip header line in file

Data Format

You can load data from a CSV with the following format:

    "metric", "value", "source", "timestamp"
    CPU, 0.1,"etl-test-red",1466406000
    CPU, 0.2,"etl-test-red",1466413200
    CPU, 0.3,"etl-test-red",1466416800
    CPU, 0.4,"etl-test-red",1466420400
    CPU, 0.5,"etl-test-red",1466424000
    CPU, 0.6,"etl-test-red",1466427600
    CPU, 0.7,"etl-test-red",1466431200
    CPU, 0.8,"etl-test-red",1466434800
    CPU, 0.9,"etl-test-red",1466438400
    CPU, 0.1,"etl-test-green","2016-06-23 1:00AM"
    CPU, 0.2,"etl-test-green","2016-06-23 2:00AM"
    CPU, 0.3,"etl-test-green","2016-06-23 3:00AM"
    CPU, 0.4,"etl-test-green","2016-06-23 4:00AM"
    CPU, 0.5,"etl-test-green","2016-06-23 5:00AM"
    CPU, 0.6,"etl-test-green","2016-06-23 6:00AM"
    CPU, 0.7,"etl-test-green","2016-06-23 7:00AM"
    CPU, 0.8,"etl-test-green","2016-06-23 8:00AM"
    CPU, 0.9,"etl-test-green","2016-06-23 9:00AM"
    CPU, 0.1,"etl-test-blue","2016-06-23 13:00"
    CPU, 0.2,"etl-test-blue","2016-06-23 14:00"
    CPU, 0.3,"etl-test-blue","2016-06-23 15:00"
    CPU, 0.4,"etl-test-blue","2016-06-23 16:00"
    CPU, 0.5,"etl-test-blue","2016-06-23 17:00"
    CPU, 0.6,"etl-test-blue","2016-06-23 18:00"
    CPU, 0.7,"etl-test-blue","2016-06-23 19:00"
    CPU, 0.8,"etl-test-blue","2016-06-23 20:00"
    CPU, 0.9,"etl-test-blue","2016-06-23 21:00"

The timestamp can be entered as unix epoch time or the formats shown
above.

Using the Tool

With a file named test.csv with the contents above the data can be
loaded and associated with the application _DOG_ONE_ by executing the
following command:

    tsp-etl csv -f test.csv  --skip-first-line -p "DOG_ONE"
