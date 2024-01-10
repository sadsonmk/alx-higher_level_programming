// fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello
// loads even when the script is in the head tag
$(function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    dataType: 'json',
    success: function (data) {
      $('#hello').text(data.hello);
    }
  });
});
