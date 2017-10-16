from sopel import module

@module.rule("Hello bot")
def hi(bot, trigger):
	bot.say('Hello, ' + trigger.nick)
	