"""
The MIT License (MIT)

Copyright (c) 2014 Dimitri John Ledkov

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import requests
class Walker:
    def __init__(self, url):
        self._url = url
        self._request = requests.get(self._url)
        self._request.raise_for_status()
        self._json = requests.get(self._url).json()
        self._resource_type = self._json.pop('resource_type_link', None)
        
    def __dir__(self):
        return super().__dir__() + list(self._json.keys())

    def __repr__(self):
        return '%s(%r)' % (self.__class__, self._url)
    
    def __getattr__(self, name):
        if name in self._json:
            value = self._json[name]
            if name.endswith('_link') and isinstance(value, str) and value.startswith('http'):
                return Walker(self._json[name])
            else:
                return value
        raise AttributeError()
