#
# Copyright 2016 BMC Software, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from tspetl import CSVTool
import argparse


class TspEtlCli(object):

    def __init__(self):
        self._parser = None
        self._subparsers = None
        self._args = None

        self._csv_parser = None
        self._db_parser = None
        self._xml_parser = None
        self._log_parser = None

        self._tool_map = {}
        self._csv_tool = CSVTool()
        self._tool_map[self._csv_tool.name] = self._csv_tool

    def _create_parser(self):
        self._parser = argparse.ArgumentParser(description="Tool to extract/transform/load into Pulse")
        self._subparsers = self._parser.add_subparsers(help='commands', dest='command_name')

        self._csv_tool.add_parser(self._subparsers)

        self._custom_parser = self._subparsers.add_parser('custom', help="import CSV file")

        self._github_parser = self._subparsers.add_parser('github', help="import data GitHub")

        self._log_parser = self._subparsers.add_parser('jira', help="import data from Jira")

        self._log_parser = self._subparsers.add_parser('log', help="import log file")
        self._log_parser.add_argument('-f', '--file', metavar="path", help="Path to file to import", required=False)

        self._sales_force_parser = self._subparsers.add_parser('salesforce', help="import data from Sales Force")

        self._snmp_parser = self._subparsers.add_parser('snmp', help="import SNMP data")

        self._snmp_parser = self._subparsers.add_parser('stock', help="import stock price and volume")

        self._syslog_parser = self._subparsers.add_parser('syslog', help="import syslog file")

        self._twitter_parser = self._subparsers.add_parser('twitter', help="import data from Twitter")

        self._weather_parser = self._subparsers.add_parser('weather', help="import weather data from Open Weather Map")

        self._xml_parser = self._subparsers.add_parser('xml', help="import xml file")
        self._xml_parser.add_argument('-f', '--file', metavar="path", help="Path to XML file to import", required=False)

    def _parse_arguments(self):
        self._create_parser()
        args = self._parser.parse_args()
        print(args)
        self._tool_map[args.command_name].run(args)

    def run(self):
        self._parse_arguments()


def main():
    cli = TspEtlCli()
    cli.run()


if __name__ == '__main__':
    main()
