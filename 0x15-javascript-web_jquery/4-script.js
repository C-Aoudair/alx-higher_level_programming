let header = $('header');
$('#toggle_header').click(function() {
	if (header.hasClass('red')) {
		header.toggleClass('green');
	} else {
		header.addClass('red');
	}
});
