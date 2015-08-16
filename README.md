# phaser-server

A simple development web server for phaser.js in Python/Flask.

Developed on OSX. Works on Linux.
Never tested on Windows.

####Requirements

Python 2.7
Flask - http://flask.pocoo.org/


####Version of Phaser included:

This includes version 2.4.2 in minified form.
Version released on 29th July 2015.


###Setup

With a terminal window:
- Go to your working directory.
- Type: pip install -r requirements.txt This will install all dependecies for you.
- Type python main.py to start the server.
- Open a browser window and navigate to http://127.0.0.1:5000/
- If you need to change the PORT:
    - Open the file called development_settings.cfg.
	- Add a new variable called "PORT" followed by the port number you wish to use now. Example:
	    PORT=8080
- To quite the server process hit ctrl-c.



###Templates

This uses a templating system called Jinja2.
http://jinja.pocoo.org/


#####Developing

A **game.js** file is included in the

    static/js/

directory for convenience. It is referenced in the layout template.
A **div** with an **id** of **game** is included in the file **index.html**.
All you need to do is add your code to the game.js file. 