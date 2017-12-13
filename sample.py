# -*- coding: utf-8 -*-
"""
Sample code for using ciscosparkbot
"""

import os
from ciscosparkbot import SparkBot

__author__ = "scoutst"
__author_email__ = "tungnx@dts.com.vn"
__copyright__ = "Fork from Copyright (c) 2016 Cisco Systems, Inc."
__license__ = "Apache 2.0"

# Retrieve required details from environment variables
bot_email = os.getenv("tungnx@dts.com.vn")
spark_token = os.getenv("Njk3M2UwOWItMjJmYi00MjY3LWFhZDEtMjA5YjQyMWEzYTQ3ZjE0NWZkMzItMDdi")
bot_url = os.getenv("scoutst.herokuapp.com")
bot_app_name = os.getenv("HerokuBot")

def do_something(incoming_msg):
    """
    Sample function to do some action.
    :param incoming_msg: The incoming message object from Spark
    :return: A text or markdown based reply
    """
    return "i did what you said - {}".format(incoming_msg.text)

# Create a new bot
bot = SparkBot(bot_app_name, spark_bot_token=spark_token,
               spark_bot_url=bot_url, spark_bot_email=bot_email, debug=True)

# Add new command
bot.add_command('/dosomething', 'help for do something', do_something)

# Run Bot
bot.run(host='0.0.0.0', port=5000)
