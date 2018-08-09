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

inside_movie = {
    "title": "Inside Out",
    "id": "tt2096673",
    "year_released": 2012,
    "rating": "PG",
    "score": 7.5,
    "out_of": 10,
    "reviews": 463787
}

shrek_movie = {
    "title": "Shrek",
    "id": "tt0126029",
    "year_released": 2001,
    "rating": "PG",
    "score": 7.9,
    "out_of": 10,
    "reviews": 531432
    "genre": ["Animation", "Adventure", "Comedy"]
}

movies = [shrek_movie, inside_movie]

user = raw_input('Enter a genre: ').capitalize()

bestMovie = {'title':"none", "rating":0}

for i in movies:
    if user in i["genre"]:
        if bestMovie["rating"]< i["rating"]:
            bestMovie["rating"] = i["rating"]
            bestMovie["title"] = i["title"]

print bestMovie["title"]
