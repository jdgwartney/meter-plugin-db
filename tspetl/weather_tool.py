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
from tspetl import ETLCollector
from tspetl import ETLTool


class WeatherCollector(ETLCollector):

    def __init__(self, sink, **kwargs):
        super(WeatherCollector, self).__init__(sink)
        self._api_key = hasattr(kwargs, 'api_key')
        self._cities = hasattr(kwargs, 'cities')
        se

    def collect(self):
        pass


class WeatherTool(ETLTool):

    def __init__(self):
        pass

    @property
    def name(self):
        return 'weather'

    @property
    def help(self):
        return 'Collects weather measurements from a city and optional country code.'

    def add_parser(self, sub_parser):
        super(WeatherTool, self).add_parser(sub_parser)
        self._parser.add_argument('-c', '--city-name', dest='city_name', metavar="city_name", help="Name of a city with an optional country code", required=False)
        self._parser.add_argument('-i', '--interval', dest='interval', metavar="seconds",
                                  help="How often to collect in each API call", required=False)
        self._parser.add_argument('-k', '--api-key', dest='api_key', metavar="key", required=True,
                                  help="Open Weather Map API Key")

    def _handle_arguments(self, args):
        pass

    def run(self, args, sink):
        collector = WeatherCollector(sink, )

        while True:
            pass

