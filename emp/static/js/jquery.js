$(document).ready(function(){
  $("#myInput").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#myTable tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});


//$(document).ready(function(){
//  $("#myInput").on("keyup", function() {
//    var value = $(this).val().toLowerCase();
//    $("#myDIV *").filter(function() {
//      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
//    });
//  });
//});