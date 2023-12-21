$(document).ready(function(){

  function ajax_calendar(id,value){
    let calendar = document.getElementById('calendar_conteiner');
    $.ajax({
        url:'/calendar/'+id,
        type: 'POST',
        data: {'id_post':value},
        success: function(response){
            console.log(response);
            calendar.innerHTML=response;
        }
    });
  }

  $('.showCalendar').on('click', function(){
    ajax_calendar($(this).attr('id'),$(this).attr('value'))
  })
});

