/**
 * @file 2-script.js
 * @author TheWatcher01
 * @date 30-05-2024
 * @description This script updates the text color of the HTML tag HEADER to red (#FF0000)
 * when the user clicks on the tag DIV#red_header
 */

/* eslint-env browser */

// Get the header element
const headerElement = document.querySelector('header');

// Get the button element
const redHeaderButton = document.getElementById('red_header');

// Add a click event listener to the button
redHeaderButton.addEventListener('click', function () {
  // Add the 'red' class to the header element
  headerElement.classList.add('red');
});
