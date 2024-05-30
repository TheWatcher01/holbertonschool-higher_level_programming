/**
 * @file 1-script.js
 * @author TheWatcher01
 * @date 30-05-2024
 * @description
 */

// Get the header element
const headerElement = document.querySelector('header');

const redHeaderButton = document.getElementById('red_header');

redHeaderButton.addEventListener('click', function () {
  // Change the color of the header element to red
  headerElement.style.color = '#FF0000';
});
