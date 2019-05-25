# -*- coding: utf-8 -*-
def onQQMessage(bot, contact, member, content):
    if member == 'None':
        if content == '-happy new year':
            bot.Update('buddy')
            friends = bot.List('buddy')
            for friend in friends:
                bot.SendTo(friend, '新年快乐，狗年大吉', resendOn1202=False)

        if content.find('新年快乐') >= 0:
            bot.SendTo(contact, '哈哈哈，我只是一个群发消息的机器人', resendOn1202=False)

        if content.find('狗年大吉吧')>= 0:
            bot.SendTo(contact, '那也祝你狗年大吉吧', resendOn1202=False)

        if content.find('发红包')>= 0:
            bot.SendTo(contact, '要我发红包？不存在的，没有实名，领红包都领不了！', resendOn1202=False)