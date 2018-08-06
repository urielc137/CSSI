// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

console.log("Running Click Events Script");
const colors=['red','pink','orange'];
let box1 = document.querySelector('#box1');
let box2 = document.querySelector('#box2');
let box3 = document.querySelector('#box3');
let box4 = document.querySelector('#box4');
let box5 = document.querySelector('#box5');
let rect = document.querySelector('#rect');
let box6 = document.querySelector('#box6');

box1.addEventListener('click', switchcolor0);

function switchcolor0 (){
  box1.style.backgroundColor=colors[0];
  box2.style.backgroundColor=colors[0];
  box3.style.backgroundColor=colors[0];
}

box2.addEventListener('click', switchcolor1);

function switchcolor1 (){
  box1.style.backgroundColor=colors[1];
  box2.style.backgroundColor=colors[1];
  box3.style.backgroundColor=colors[1];
}

box3.addEventListener('click', switchcolor2);

function switchcolor2 (){
  box1.style.backgroundColor=colors[2];
  box2.style.backgroundColor=colors[2];
  box3.style.backgroundColor=colors[2];
}
