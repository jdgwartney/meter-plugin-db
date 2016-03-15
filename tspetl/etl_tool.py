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


class ETLTool(object):

    def __init__(self):
        self._parser = None
        self._email = None
        self._api_token = None

    @property
    def name(self):
        return None

    @property
    def help(self):
        return None

    def add_parser(self, sub_parser):
        self._parser = sub_parser.add_parser(self.name, help=self.help)
        self._parser.add_argument('-e', '--e-mail', dest='email', metavar='email')
        self._parser.add_argument('-t', '--api-token', dest='api_token', metavar='api_token')

    def handle_arguments(self, args):
        if args.email is not None:
            self._email = args.email

        if args.batch_count is not None:
            self._batch_count = args.batch_count

    def run(self, args):
        pass
