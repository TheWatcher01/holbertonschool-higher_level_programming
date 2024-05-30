/**
 * @file 4-script.js
 * @author TheWatcher01
 * @date 30-05-2024
 * @description This script adds a new item to a list when the user clicks on the tag DIV#add_item
 */

/* eslint-env browser */

// Get the button element
const addItem = document.getElementById('add_item');

// Get the list element
const myList = document.querySelector('ul.my_list');

// Add a click event listener to the button
addItem.addEventListener('click', function () {
  // Create a new list item
  const newItem = document.createElement('li');

  // Set the text content of the new item
  newItem.textContent = 'Item';

  // Add the new item to the list
  myList.appendChild(newItem);
});
