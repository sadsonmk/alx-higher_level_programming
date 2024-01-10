// fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json

$(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    dataType: 'json',
    success: function (data) {
      $.each(data.results, function (key, movie) {
        $('<li>').text(movie.title).appendTo('#list_movies');
      });
    }
  });
});
