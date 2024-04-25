var temperatureChart = null
var currentRoom = null

const fetchDevices = () => fetch("devices")
  .then(res => res.json())
    .then(data => {
        data.devices.forEach(todo => {
          let option = new Option(todo.name, todo.name)
          console.log(option)
          document.getElementById('devices').add(option)
          currentRoom = todo.name
        });
  });




const csvToChartData = csv => {
  const lines = csv.trim().split("\n");
  return lines.map(line => {
    const [date, temperature] = line.split(",");
    return {
      x: date,
      y: temperature
    };
  });
};

function fetchCSV() {
  fetch(currentRoom)
  .then(data => data.text())
  .then(csv => {
    temperatureChart.data.datasets[0].data = csvToChartData(csv);
    temperatureChart.update();
    timeout = setTimeout(fetchCSV, 60000); // double tap?
  });
}

function createChart(room) {

  currentRoom = room

  console.log("Changing to " + currentRoom);

  const config = {
    type: 'line',
    data: {
      labels: [],
      datasets: [{
        data: [],
        label: room + ' Readings',
        borderColor: "#3e95cd",
        fill: false
      }]
    },
    options: {
      scales: {
        xAxes: [{
          type: 'time',
          distribution: 'linear',
        }],
        title: {
          display: false,
        },
        legend: {
          display: false,
        }
      }
    }
  };

  const ctx = document.getElementById('temps').getContext('2d');
  temperatureChart = new Chart(ctx, config);

  fetchCSV();

}

