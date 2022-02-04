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
            let loc = 'workout.html' + "?" + "title=" + info.event.title + "&" + "startTime=" + info.event.startStr + "&" + "endTime=" + info.event.endStr;
            window.location.href = loc;
        },
        initialView: 'dayGridWeek',
        headerToolbar: {
            center: 'addEventButton'
        },
        customButtons: {
            addEventButton: {
                text: 'Go to leaderboard',
                click: function() {
                    window.location.href = 'frontend/leaderboard.html'
              }
            }
          }
    });
    calendar.render();

    let workoutName = prompt("Enter workout name", "base");
    let requestURL = window.location.origin + "/" + workoutName + ".json";
    let request = new XMLHttpRequest();
    request.open('GET', requestURL);
    request.responseType = 'json';
    request.send();
    request.onload = function() {
      const json = request.response;
      console.log(json);
      renderEvents(calendar, json);
    }

    window.onload = setTimeout(function(){
        prompt('Time to do desk pushups! Enter "done" when done or "skip" to skip this workout');
        alert('+10 points! Check the leaderboard to see where you stand');
    }, 5000);
});

