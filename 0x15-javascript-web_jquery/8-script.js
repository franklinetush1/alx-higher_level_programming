$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
      if (data.results && data.results.length > 0) {
        const movies = data.results;        
        const listMovies = $("#list_movies");        
        movies.forEach(function (movie) {
          const title = movie.title;
          listMovies.append(`<li>${title}</li>`);
        });}
});
