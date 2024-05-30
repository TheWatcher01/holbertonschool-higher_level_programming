/**
 * @file 100-script.js
 * @author TheWatcher01
 * @date 30-05-2024
 * @description This script adds, removes, and clears list items in the element with id my_list based on user clicks
 */

/* eslint-env browser */

// Get the button elements
const addItem = document.getElementById('add_item');
const removeItem = document.getElementById('remove_item');
const clearList = document.getElementById('clear_list');

// Get the list element
const myList = document.querySelector('ul.my_list');

// Add a click event listener to the add_item button
addItem.addEventListener('click', function () {
  // Create a new list item
  const newItem = document.createElement('li');

  // Set the text content of the new item
  newItem.textContent = 'Item';

  // Add the new item to the list
  myList.appendChild(newItem);
});

// Add a click event listener to the remove_item button
removeItem.addEventListener('click', function () {
  // Check if the list has any items
  if (myList.lastElementChild) {
    // If it does, remove the last item from the list
    myList.removeChild(myList.lastElementChild);
  }
});

// Add a click event listener to the clear_list button
clearList.addEventListener('click', function () {
  // Clear all items from the list
  myList.innerHTML = '';
});
