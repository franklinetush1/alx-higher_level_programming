  $(document).ready(function() {
    const url = 'https://www.fourtonfish.com/hellosalut/?';    
    function fetchTranslation() {
      $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function(data) {
        $('DIV#hello').html(data.hello);
      }).fail(function(xhr, status, error) {
        console.error("Error fetching translation:", error);
      });
    }    
    $("#btn_translate").click(function() {
      fetchTranslation();
    });
    $("#language_code").keypress(function(event) {
      if (event.which === 13) { // 13 is the keycode for Enter key
        fetchTranslation();
      }
    });
  });
