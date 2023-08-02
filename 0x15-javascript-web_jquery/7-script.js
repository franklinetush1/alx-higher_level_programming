$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (obj) {
  $('DIV#character').text(obj.name);
});
