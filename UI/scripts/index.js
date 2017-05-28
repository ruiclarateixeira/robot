var connection = null;

function connect() {
  var ip = $('#ip-add').val();
  connection = new WebSocket("ws://" + ip + ":5001");

  connection.onopen = function () {
    connection.send('Ping');
  };

  connection.onerror = function (error) {
    console.log('WebSocket Error ' + error);
  };

  connection.onmessage = function (e) {
    console.log('Server: ' + e.data);
  };
}

function moveForward() {
  connection.send("w");
}

function moveBackward() {
  connection.send("s");
}

function turnRight() {
  console.log("Turning right");
}

function turnLeft() {
  console.log("Turning left");
}

function stop() {
  connection.send("p");
}

function init() {
  $("#up").mousedown(moveForward).mouseup(stop);
  $("#down").mousedown(moveBackward).mouseup(stop);
}

$(init);
