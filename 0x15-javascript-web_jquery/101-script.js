// adds, removes and clears LI elements from a list when the user clicks
//
$(function () {
  const newElem = '<li>Item</li>';
  $('#add_item').click(function () {
    $(newElem).appendTo('ul.my_list');
  });
  $('#remove_item').click(function () {
    $('ul.my_list > li').last().remove();
  });
  $('#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
