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

// Use querySelector to store the div in a variable.
const colors=['red','green','blue', 'white'];
let redButton = document.querySelector('#red');
let greenButton = document.querySelector('#green');
let blueButton = document.querySelector('#blue');
let clearButton = document.querySelector('#clear');
let box = document.querySelector('#responseBox');

// Use addEventListener to respond to a click event.
redButton.addEventListener('click', (switchcolor0) => {
  console.log("You clicked the red button!");
})

greenButton.addEventListener('click', (switchcolor1) => {
  console.log("You clicked the green button!");
})

blueButton.addEventListener('click', (switchcolor2) => {
  console.log("You clicked the blue button!");
})

clearButton.addEventListener('click', (switchcolor3) => {
  console.log("You clicked the clear button!");
})

redButton.addEventListener('click', switchcolor0);

function switchcolor0 (){
  redButton.style.backgroundColor=colors[0];
  box.style.backgroundColor=colors[0];
}

greenButton.addEventListener('click', switchcolor1);

function switchcolor1 (){
  greenButton.style.backgroundColor=colors[1];
  box.style.backgroundColor=colors[1];
}

blueButton.addEventListener('click', switchcolor2);

function switchcolor2 (){
  blueButton.style.backgroundColor=colors[2];
  box.style.backgroundColor=colors[2];
}

clearButton.addEventListener('click', switchcolor3);

function switchcolor3 (){
  clearButton.style.backgroundColor=colors[3];
  box.style.backgroundColor=colors[3];
}