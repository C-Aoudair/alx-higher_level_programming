$(document).ready(function() {
	$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json',
	function(response) {
		const movies = response.results;
		let item;
		for (let i = 0; i < movies.length; i++) {
			item = `<li>${movies[i].title}</li>`;
			$('#list_movies').append(item);
		}
	});
});