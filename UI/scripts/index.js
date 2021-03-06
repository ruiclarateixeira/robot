var connection = null;

function updateConnectionStatus(newStatus) {
   $("#connection-status").text(newStatus);
}

function connect() {
  var ip = $('#ip-add').val();
  connection = new WebSocket("ws://" + ip + ":5001");

  connection.onopen = function () {
      updateConnectionStatus("Connected!");
  };

  connection.onerror = function (error) {
    console.log('WebSocket Error ' + error);
  };

  connection.onmessage = function (e) {
    console.log('Server: ' + e.data);
  };
}

function moveForward(event) {
  connection.send("w");
}

function moveBackward(event) {
  connection.send("s");
}

function turnRight(event) {
  connection.send("d");
}

function turnLeft(event) {
  connection.send("a");
}

function stop(event) {
  connection.send("p");
}

function init() {
  $("#up").bind("touchstart", moveForward).bind("touchend", moveForward).mousedown(moveForward).mouseup(stop);
  $("#down").bind("touchstart", moveBackward).bind("touchend", moveBackward).mousedown(moveBackward).mouseup(stop);
  $("#left").bind("touchstart", turnLeft).bind("touchend", turnLeft).mousedown(turnLeft).mouseup(stop);
  $("#right").bind("touchstart", turnRight).bind("touchend", turnRight).mousedown(turnRight).mouseup(stop);
}

$(init);
