# Mef Bot

A simple bot that automatically connects to my university moodle server, views course information and automatically attends them.

## Getting Started

This bot can be run on Windows, Linux and OSX. To get started with using it, clone this repository.

Before you can even run the program, you will need to change the `moodle` variable located on line 8 of the `loginbot.py` file.
In order to acces specific courses, you will also need to change the course variables located under the `moodle` variable.


**Note: To use the developmental google meets feature you have to create a new firefox profile. [This guide](https://www.google.com) explains how to do just that. If you want the program to work out of the box, name your profile "GoogleMeet"*

### Prerequisites



```
Python 3.x
pip
selenium
```

### Installing

To get started with using this bot, run `git clone git@github.com:showtimezz/mefBot.git` from your terminal. 


## Deployment

You can run this program in a headless state by adding the `headless` option on the web driver located in `loginbot.py` 
There have been sevral reported issues with this method, which is why it is't enabled by default. To learn more, check the 
[Issues page](https://github.com/showtimezz/mefBot/issues/). 

## Contributing

The easiest way to contribute to the development of this program is to take a quick look at the [Issues page](https://github.com/showtimezz/mefBot/issues/). 

You can also take a look at our

## Coming soon features
* Google Meet support
* Zoom Support
* Teams support

And help here
## License

This project is licensed under the MIT License.

