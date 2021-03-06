# Robot

This project is a small robot powered by raspberry pi. It's currently fully controlled but it has high hopes of becoming somewhat autonomous in the future.

## Hardware
* Raspberry Pi 1 B
* Voltage Regulator (5-35v -> 0-33v)
* L298N Stepper Motor Driver
* Battery - 9.6v 1800mAh
* Plenty of jumper wires

## Software

### The brains
A Python application that allows control of the car via a [WebSocket]

### The face
A web app using vanilla javascript with a hint o jquery. Allows very basic moves.

## Progress so far
![Top View Picture](https://cloud.githubusercontent.com/assets/2995788/26531332/de2970ea-43de-11e7-8ecb-239c8345d136.JPG)

![Side View Picture](https://cloud.githubusercontent.com/assets/2995788/26531333/df815ae8-43de-11e7-83f7-85d30c264a38.JPG)

[WebSocket]: https://github.com/dpallot/simple-websocket-server