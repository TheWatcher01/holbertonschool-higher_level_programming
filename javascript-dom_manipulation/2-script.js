/**
 * @file 2-script.js
 * @author TheWatcher01
 * @date 30-05-2024
 * @description Script that updates the text color of the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#red_header
 */

const headerElement = document.querySelector('header');

const redHeaderButton = document.getElementById('red_header');

redHeaderButton.addEventListener('click', function () {
  headerElement.classList.add('red');
});
