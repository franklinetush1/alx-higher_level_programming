$(document).ready(function() {
        $("#add_item").click(function() {
          var newItem = "<li>Item</li>";
          $(".my_list").append(newItem);
        });

        $("#remove_item").click(function() {
          $(".my_list li:last-child").remove();
        });

        $("#clear_list").click(function() {
          $(".my_list").empty();
        });
});
