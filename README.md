#This repository is archived and will no longer receive updates.

twittertabs
===========

Simple app for keeping track of friend's activity on Twitter

Visit Twitter to read the masses; get keep tabs on your friends' tweets with Twittertabs.

Comments and suggestions welcome. Patches too!

Usage
-----

Sign up for an app at dev.twitter.com/apps, and record your API and Access Keys and Secrets.

Copy the ttabs.conf-sample file to ttabs.conf, and fill out the sections with your API and Access Keys and Secrets, and add the users you want to follow as a comma-separated list under 'users'.

After doing that, running the script should give you a list of Tweets that are less than 5 hours old posted by the users you specified.

Requirements
------------

* Python 2.7
* Tweepy module
* Time module
* ConfigParser module

Copyright Information
---------------------

Copyright (C) 2014 Chris Collins

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.
