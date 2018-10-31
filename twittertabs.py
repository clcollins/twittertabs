#!/usr/bin/env python3
#
# Twittertabs
# ===========
#
# Keep track of specific Friend's tweets so they're not lost
# in the masses
#
# Chris Collins, <christopher.collins@duke.edu>
#
# v0.2 - 2018-10-31 - Upgrade to Python3
# v0.1 - 2014-03-25
#
# Copyright (C) 2014-2018 Chris Collins
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Read Auth and Friend list from config file
# Return results of friends have posted in last 5 hours
# Run via cron 4x/day

# IMPORT FUNCTIONS
# time - for checking age of tweets
# tweepy -  for the Twitter OAuth interface <- replace with real oauth someday
# ConfigParser - for config file reading

import time
import tweepy
import configparser

# The Current Time
now = time.time()

# Parse the config file
parser = configparser.ConfigParser()
parser.read('ttabs.conf')
config = dict((section, dict((option, parser.get(section, option))
                             for option in parser.options(section)))
              for section in parser.sections())

# The users to check for new tweets
# Super ugly.  I should be ashamed.
users = [config['users']['users']][0].split(',')

# Keys/Tokens/Secrets for connecting to the Twitter API
API_KEY = config['api']['key']
API_SECRET = config['api']['secret']
ACCESS_TOKEN = config['access']['key']
ACCESS_SECRET = config['access']['secret']


# Connect to twitter API
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


def check_tweets(user):
    """ Get Tweets from this user """
    for tweet in api.user_timeline(user):
        """ If Tweet epoch time is greater than
            the current epoch time minus five hours
            (18000 seconds), then print """
        createdstr = str(tweet.created_at)
        if mkepoch(createdstr) > (int(now) - 18000):
            print(tweet.text)
            print('----------')
            print(tweet.author.screen_name)
            print(tweet.created_at)
            print('')


def mkepoch(date):
    """ Convert the 'created_at' datetime to epoch """
    pattern = '%Y-%m-%d %H:%M:%S'
    epoch = int(time.mktime(time.strptime(date, pattern)))
    return epoch


for user in users:
    check_tweets(user)
