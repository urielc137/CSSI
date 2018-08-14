#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
import webapp2
import os
import random
import jinja2
from google.appengine.api import urlfetch
import urllib
import json

URL = 'https://www.googleapis.com/customsearch/v1?'
KEY = 'AIzaSyBtGFYJwJaeNnJh0dNdt4i3MEm6TTPTGSA'
CX = '006139241214429129167:i8bcga6pwhg'

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def get_fortune():
    #add a list of fortunes to the empty fortune_list array
    fortune_list=['fortune1', 'fortune2']
    #use the random library to return a random element from the array

    random_fortune = fortune_list[random.randint(0,1)]
    return random_fortune


#remember, you can get this by searching for jinja2 google app engine
jinja_current_directory = "insert jinja2 environment variable here"


class FortuneHandler(webapp2.RequestHandler):
    def get(self):
        random_fortune = get_fortune()
        # In part 2, instead of returning this string,
        # make a function call that returns a random fortune.
        self.response.write(random_fortune)
    #add a post method
    #def post(self):
class HelloHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello World. Welcome to the root route of my app')

class GoodbyeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('My response is Goodbye World')

class SimpleUrlFetcher(webapp2.RequestHandler):
    def get(self):
        query = 'cat'
        query_params = {'key': KEY, 'cx': CX, 'q': query}
        result = urlfetch.fetch(URL + urllib.urlencode(query_params))
        if result.status_code == 200:
            self.response.write(result.status_code)
            self.response.write(result.content)
        else:
            self.response.status_code = result.status_code
#the route mapping
app = webapp2.WSGIApplication([
    #this line routes the main url ('/')  - also know as
    #the root route - to the Fortune Handler
    ('/', HelloHandler),
    ('/predict', FortuneHandler), #maps '/predict' to the FortuneHandler
    ('farewell', GoodbyeHandler),
    ('/simple', SimpleUrlFetcher)
], debug=True)
