/**
 * @file 5-script.js
 * @author TheWatcher01
 * @date 30-05-2024
 * @description This script updates the text of the header element to 'New Header!!!' when the user clicks on the tag DIV#update_header
 */

/* eslint-env browser */

// Get the button element
const updateHeader = document.getElementById('update_header');

// Get the header element
const headerElement = document.querySelector('header');

// Add a click event listener to the button
updateHeader.addEventListener('click', function () {
  // Update the text content of the header element
  headerElement.textContent = 'New Header!!!';
});
