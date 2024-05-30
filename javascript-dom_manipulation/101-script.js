/**
 * @file 101-script.js
 * @author TheWatcher01
 * @date 30-05-2024
 * @description This script fetches and displays the translation of "Hello" based on the selected language.
 */

/* eslint-env browser */

// Wait until the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function () {
  // Add a click event listener to the button with id 'btn_translate'
  document.getElementById('btn_translate').addEventListener('click', function () {
    // Get the selected language from the dropdown with id 'language_code'
    const language = document.getElementById('language_code').value;

    // Only fetch the translation if a language is selected
    if (language) {
      // Fetch the translation from the API
      fetch(`https://hellosalut.stefanbohacek.dev/?lang=${language}`)
        .then(response => {
          // Parse the response as JSON
          if (response.ok) {
            return response.json();
          } else {
            throw new Error('Error: ' + response.statusText);
          }
        })
        .then(data => {
          // Display the translation in the div with id 'hello'
          document.getElementById('hello').innerText = data.hello;
        })
        .catch(error => {
          // Log any errors
          console.error('Error:', error);
        });
    }
  });
});
