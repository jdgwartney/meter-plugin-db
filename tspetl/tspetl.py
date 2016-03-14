import argparse


class TspEtlCli(object):

    def __init__(self):
        self._parser = None
        self._subparsers = None
        self._csv_parser = None
        self._db_parser = None
        self._xml_parser = None
        self._log_parser = None

    def _create_parser(self):
        self._parser = argparse.ArgumentParser(description="Tool to extract/transform/load into Pulse")
        self._subparsers = self._parser.add_subparsers(help='commands')

        self._csv_parser = self._subparsers.add_parser('csv', help="import csv file")
        self._csv_parser.add_argument('-f', '--file', metavar="path")

        self._db_parser = self._subparsers.add_parser('db', help="import data from a database")
        self._log_parser = self._subparsers.add_parser('log', help="import log file")
        self._syslog_parser = self._subparsers.add_parser('syslog', help="import syslog file")
        self._xml_parser = self._subparsers.add_parser('xml', help="import xml file")

    def _parse_arguments(self):
        self._create_parser()
        self._parser.parse_args()

    def run(self):
        print("Running...")
        self._parse_arguments()

def main():
    cli = TspEtlCli()
    cli.run()


if __name__ == '__main__':
    main()
