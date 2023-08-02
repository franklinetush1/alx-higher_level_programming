$(document).ready(function() {
    // Function to fetch and display the translation
    function fetchTranslation() {
      const languageCode = $("#language_code").val();
      const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

      // jQuery AJAX request using get method
      $.get(apiUrl, function(data) {
        const translation = data.hello;
        $("#hello").text(translation);
      }).fail(function(xhr, status, error) {
        console.error("Error fetching translation:", error);
      });
    }

    // Attach click event handler to #btn_translate
    $("#btn_translate").click(function() {
      fetchTranslation();
    });
  });
