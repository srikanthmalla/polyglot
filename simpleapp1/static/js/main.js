var ALARM_URL = "{% url 'subs' %}";
function refresh() {
  $.ajax({
  url: ALARM_URL,
  success: function(data) {
    $('#right').html(data);
  }
 });
};

$(document).ready(function ($) {
  refresh();
  var int = setInterval("refresh()", 3000);
}