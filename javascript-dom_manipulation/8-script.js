/**
 * @file 8-script.js
 * @author TheWatcher01
 * @date 30-05-2024
 * @description This script fetches the translation of "hello" in French and displays it in the element with id hello when the document is fully loaded
 */

/* eslint-env browser */

// Add a DOMContentLoaded event listener to the document
document.addEventListener('DOMContentLoaded', function () {
  // Get the hello element
  const helloElement = document.getElementById('hello');

  // Fetch the translation of "hello" in French
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
      // Display the translation in the hello element
      helloElement.textContent = data.hello;
    })
    .catch(error => {
      // Log any errors that occur during the fetch
      console.error('Error fetching translation:', error);
    });
});
