function findGetParameter(parameterName) {
    var result = null,
        tmp = [];
    location.search
        .substr(1)
        .split("&")
        .forEach(function (item) {
          tmp = item.split("=");
          if (tmp[0] === parameterName) result = decodeURIComponent(tmp[1]);
        });
    return result;
}

let title = findGetParameter("title")
let timeStart = new Date(findGetParameter("startTime"));
let timeEnd = new Date(findGetParameter("endTime"));
let diff = (timeEnd - timeStart)/3.6e+6

window.addEventListener('DOMContentLoaded', (event) => {
    const titleElement = document.getElementById("title");
    titleElement.innerHTML = "Workout: " + title;

    const dayElement = document.getElementById("day");
    dayElement.innerHTML = "Day: " + timeStart.toLocaleString('en-us', {  weekday: 'long' });

    const timeEndElement = document.getElementById("duration");
    timeEndElement.innerHTML = "Duration: " + diff + " Hour(s)";
});
