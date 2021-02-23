function renderEvents(calendar, workouts) {
    workouts.forEach(function(workout) {
        calendar.addEvent(
              {
                  title: workout['name'],
                  daysOfWeek: workout['days'],
                  startTime: workout['timeStart'],
                  endTime: workout['timeEnd']
              }
        );
    });
}

document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        eventClick: function(info) {
            console.log('Event: ' + info.event.title);
            let loc = 'workout/' + info.event.title
            window.location.href = loc;
        },
        initialView: 'dayGridWeek',
        headerToolbar: {
            center: 'addEventButton'
        },
        customButtons: {
            addEventButton: {
                text: 'add event...',
                click: function() {
                    var dateStr = prompt('Enter a time in 24:00 hour format:');
                    var day = prompt('Enter what day ');

                    if (!isNaN(date.valueOf())) { // valid?
                      calendar.addEvent({
                        title: 'dynamic event',
                        start: date,
                        allDay: true
                      });
                      alert('Great. Now, update your database...');
                } else {
                      alert('Invalid date.');
                }
              }
            }
          }
    });
    calendar.render();

    let requestURL = 'http://127.0.0.1:8000/workouts.json';
    let request = new XMLHttpRequest();
    request.open('GET', requestURL);
    request.responseType = 'json';
    request.send();
    request.onload = function() {
      const json = request.response;
      console.log(json);
      renderEvents(calendar, json);
    }
});

