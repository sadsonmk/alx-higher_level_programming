// fetches and prints how to say “Hello” depending on the language

$(function () {
  $('#btn_translate').click(getTranslated);
  $('language_code').keypress(function () {
    if (event.keyCode === 13) {
      getTranslated();
    }
  });

  function getTranslated () {
    const value = $('#language_code').val();
    $.ajax({
      url: `https://hellosalut.stefanbohacek.dev/?lang=${value}`,
      success: function (data) {
        $('#hello').text(data.hello);
      }
    });
  }
});
