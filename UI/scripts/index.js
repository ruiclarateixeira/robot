function connect() {
  var connection = new WebSocket('ws://localhost:5001');

  connection.onopen = function () {
    connection.send('Ping'); // Send the message 'Ping' to the server
  };
}

function moveForward() {
  console.log("Moving forward");
}

function moveBackward() {
  console.log("Moving backward");
}

function turnRight() {
  console.log("Turning right");
}

function turnLeft() {
  console.log("Turning left");
}
