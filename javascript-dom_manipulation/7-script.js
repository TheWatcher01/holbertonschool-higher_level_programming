/**
 * @file 7-script.js
 * @author TheWatcher01
 * @date 30-05-2024
 * @description Fetches and lists the titles of all movies from the SWAPI and displays them in the element with id list_movies
 */

/* eslint-env browser */

// Get the list_movies element
const listMoviesElement = document.getElementById('list_movies');

// Fetch the list of movies from the SWAPI
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    // Get the list of movies from the response data
    const movies = data.results;

    // For each movie in the list of movies
    movies.forEach(movie => {
      // Create a new list item
      const listItem = document.createElement('li');

      // Set the text content of the list item to the title of the movie
      listItem.textContent = movie.title;

      // Add the list item to the list_movies element
      listMoviesElement.appendChild(listItem);
    });
  })
  .catch(error => {
    // Log any errors that occur during the fetch
    console.error('Error fetching movies:', error);
  });
