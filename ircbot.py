from willie import module
import datetime
import random

import os

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alliance_auth.settings")

#from services.managers.openfire_manager import OpenfireManager


# @module.rule('hello!?')
# def hi(bot, trigger):
#    bot.say('Hi ' + trigger.nick + ", I'm a bot")


@module.rule('.')
def ping(bot, trigger):
	if trigger.nick == "FleetBot":
		# if unicode(trigger.raw).find(
		print trigger.raw
		message = unicode(trigger.raw)
		formatted_message = message.split("] ", 1)
		print formatted_message[1] + "\nSent at: "  + datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S") + " #####\n##### Replies are NOT monitored #####\n"
		#OpenfireManager.send_broadcast_threaded('corp_nex_exercitus', str(trigger.event), )
		# bot.say('you sent a broadcast, ' + trigger.nick)
	

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
