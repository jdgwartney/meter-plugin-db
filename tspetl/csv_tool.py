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
from tspetl import ETLTool
from tspapi import API


class CSVTool(ETLTool):
    def __init__(self):
        super(CSVTool, self).__init__()
        self._file_path = None
        self._batch_count = None
        self._name = 'csv'
        self._help = 'Import CSV file'

    @property
    def name(self):
        return 'csv'

    @property
    def hep(self):
        return 'Import CSV file'

    def add_parser(self, sub_parser):
        super(CSVTool, self).add_parser(sub_parser)
        self._parser.add_argument('-f', '--file', dest='file_path', metavar="file_path", help="Path to file to import", required=False)
        self._parser.add_argument('-b', '--batch', dest='batch_count', metavar="batch_count",
                                  help="How measurements to send in each API call", required=False)

    def handle_arguments(self, args):
        super(CSVTool, self).handle_arguments(args)
        if args.file_path is not None:
            self._file_path = args.file_path

        if args.batch_count is not None:
            self._batch_count = args.batch_count

    def run(self, args):
        self.handle_arguments(args)
        api = API()
