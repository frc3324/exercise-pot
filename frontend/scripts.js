let requestURL = 'http://127.0.0.1:8000/example.json';
let request = new XMLHttpRequest();
request.open('GET', requestURL);
request.responseType = 'json';
request.send();
request.onload = function() {
  const json = request.response;
  loadPage(json);
}

function loadPage(json) {
    const header = document.getElementById("name");
    header.innerHTML = json['name'];

    const daysElem = document.getElementById("days");
    const days = json['days'];
    console.log(days);
    days.forEach(function(day) {
        const dayElem = document.createElement('p');
        dayElem.innerHTML = day;
        daysElem.appendChild(dayElem);
    });
}
