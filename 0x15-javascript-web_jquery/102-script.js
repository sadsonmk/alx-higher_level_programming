// fetches and prints how to say “Hello” depending on the language

$(function () {
  $('#btn_translate').click(function () {
    const value = $('#language_code').val();
    $.ajax({
      url: `https://hellosalut.stefanbohacek.dev/?lang=${value}`,
      dataType: 'json',
      success: function (data) {
        $('#hello').text(data.hello);
      }
    });
  });
});
