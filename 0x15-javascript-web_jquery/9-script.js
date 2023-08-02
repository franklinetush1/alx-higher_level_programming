$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
      const translation = data.hello;
      $("DIV#hello").text(translation);
});
