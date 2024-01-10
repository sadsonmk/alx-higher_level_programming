// toggles the class of the <header> element when the user clicks on the tag DIV#toggle_header
// If the current class is red, when the user click on DIV#toggle_header, the class must be updated to green ; and the reverse.
$(function () {
  $('toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
});
