// adds a <li> element to a list when the user clicks on the tag DIV#add_item

$(function () {
  const elem = '<li>Item</li>';
  $('#add_item').click(function () {
    $('ul.my_list').append(elem);
  });
});
