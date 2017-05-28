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
  connection.send("d");
}

function turnLeft() {
  connection.send("a");
}

function stop() {
  connection.send("p");
}

function init() {
  $("#up").mousedown(moveForward).mouseup(stop);
  $("#down").mousedown(moveBackward).mouseup(stop);
  $("#left").mousedown(turnLeft).mouseup(stop);
  $("#right").mousedown(turn_right).mouseup(stop);
}

$(init);
