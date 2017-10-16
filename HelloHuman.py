import sopel.module

@sopel.module.commands('initialise')
def initialise(bot, trigger):
	bot.say("Hello Human")
	