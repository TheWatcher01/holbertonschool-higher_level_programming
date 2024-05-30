/**
 * @file 6-script.js
 * @author TheWatcher01
 * @date 30-05-2024
 * @description Fetches the character name from the SWAPI and displays it in the element with id character
 */

/* eslint-env browser */

// Get the character element
const characterElement = document.getElementById('character');

// Fetch the character name from the SWAPI
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    // Display the character name in the character element
    characterElement.textContent = data.name;
  })
  .catch(error => {
    // Log any errors that occur during the fetch
    console.error('Error fetching character:', error);

    // Display an error message in the character element
    characterElement.textContent = 'Error fetching character';
  });
