# IOBuzz - Make your Buzz Controllers IOT Devices

This project allows you to turn your Playstation Buzz Controllers into IOT devices by just connecting them
to a Raspberry Pi or any other computer running this application.

Why would you want that?

Well, for sure you won't be using it to monitor your house nor to spy on anyone as they don't have embedded cameras
or microphones but you can make some nice Christmas Lights controlled by your smartphone or use them to play games
on a web browser without having to connect them to a computer or a Smart TV.

My initial idea with this project was to develop a quiz for a Smart TV where you could use your old Buzzers to answer
some trivia questions or custom quizzes but one disadvantage of connecting these controllers directly to the TV is
that despite you could technically read inputs from them using the
[Gamepad API](https://developer.mozilla.org/en-US/docs/Web/API/Gamepad_API/Using_the_Gamepad_API)
you would not be able to turn their lights on and off at will.

That project is still going but for now this is all I have.


## Getting started

### Requirements

This project assumes you are running a socket.io server somewhere on the Internet.

I have created a sample project [here](https://github.com/dmpasilva/iobuzz-server).
If you change the server configuration, namespace or messages, you will need to make changes to the application
code as well.


### Installing required dependencies

First, start by cloning this project.

Assuming you are using a Raspberry Pi running Raspbian, run the following commands to install all the required
system packages:

```
$ sudo apt install python3-venv libudev-dev libusb-1.0-0-dev
```

After that, create a virtual environment for Python and install all dependencies:

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

That's it!


### Configuring the application

You can set up your configuration by editing the `config.py` file in the `buzz_iot` directory.

You can list your USB Device Vendor ID and Device ID by running the following command:

```
$ lsusb
```


## Running the application

Here, you have two options: either give your current user permissions to read from USB devices or run the script
as root.

If you are as lazy as me, here's the quickest way:

```
$ sudo su -
# cd /path/to/the/project
# source venv/bin/activate
# python main.py
```


## Contributions and criticism

Yeah, I know the code is not the best.

But go ahead: fork it and send a Pull Request with your changes and improvements!


## Special thanks

This project was based on the original concepts explained in the following articles:

* [Raspberry Pi Quiz Game using the Buzz Controllers](https://pimylifeup.com/raspberry-pi-quiz-game-buzz-controllers/) ([source](https://github.com/pimylifeup/Raspberry-Pi-Quiz-Game-Buzz-Controllers))
* [Creating an online quiz game using Node.js, Hyperdev, PlayStation Buzz controllers, Raspberry PI and Nfield](https://www.hakantuncer.com/2016/09/07/creating-an-online-quiz-game-using-node-dot-js/)