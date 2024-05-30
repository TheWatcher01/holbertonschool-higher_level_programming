/**
 * @file 1-script.js
 * @author TheWatcher01
 * @date 30-05-2024
 * @description This script changes the color of the header element to red when the button is clicked.
 */

/* eslint-env browser */

// Get the header element
const headerElement = document.querySelector('header');

// Get the button element
const redHeaderButton = document.getElementById('red_header');

// Add a click event listener to the button
redHeaderButton.addEventListener('click', function () {
  // Change the color of the header element to red
  headerElement.style.color = '#FF0000';
});
