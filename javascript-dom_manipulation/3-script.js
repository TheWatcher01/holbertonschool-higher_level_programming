/**
 * @file 3-script.js
 * @author TheWatcher01
 * @date 30-05-2024
 * @description This script toggles the class of the header element between red and green when the user clicks on the tag DIV#toggle_header
 */

/* eslint-env browser */

// Get the button element
const toggleHeader = document.getElementById('toggle_header');

// Get the header element
const headerElement = document.querySelector('header');

// Add a click event listener to the button
toggleHeader.addEventListener('click', function () {
  // Check if the header element has the class 'red'
  if (headerElement.classList.contains('red')) {
    // If it does, remove the 'red' class and add the 'green' class
    headerElement.classList.remove('red');
    headerElement.classList.add('green');
  } else {
    // If it doesn't, remove the 'green' class and add the 'red' class
    headerElement.classList.remove('green');
    headerElement.classList.add('red');
  }
});
