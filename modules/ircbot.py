from willie import module
import datetime
import random

import os
import sys

# sys.path.append(‘/path/to/allianceauth’)

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alliance_auth.settings")

#from services.managers.openfire_manager import OpenfireManager


# @module.rule('hello!?')
# def hi(bot, trigger):
#    bot.say('Hi ' + trigger.nick + ", I'm a bot")
history = []

@module.rule('.')
def ping(bot, trigger):
	if trigger.nick == "FleetBot":
		message = unicode(trigger.raw)
		unformatted_message = message.split("] ", 1)
		if len(unformatted_message) >= 2:
			formatted_message = unformatted_message[1] + "\nSent at: "  + datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S") + " #####\n##### Replies are NOT monitored #####\n"
			print formatted_message
			#OpenfireManager.send_broadcast_threaded('AllianceMember', formatted_message, )
			# bot.say('you sent a broadcast, ' + trigger.nick)
			# for x in history[-5:-0]
			if len(history) < 5:
				history.append(formatted_message)
			else:
				history.pop(0)
				history.append(formatted_message)
	
			
@module.commands('history')
def history(bot, trigger):
	if len(history) > 0:
		for m in history:
        		bot.msg(trigger.user, m)
        else:
        	bot.msg(trigger.user, "No pings recorded")

@module.commands('9/13')
def nine_thirteen(bot, trigger):
	bot.say('A DAY THAT WILL LIVE IN INFAMY')
	bot.say('https://zkillboard.com/br/28683/')


@module.commands('8ball')
def eight_ball(bot, trigger):
        ball = random.randrange(0,3)
	if ball == 0:
		bot.say(trigger.nick + ', No')
	elif ball == 1:
		bot.say(trigger.nick + ', Yes')
	elif ball == 2:
		bot.say(trigger.nick + ', Maybe')
