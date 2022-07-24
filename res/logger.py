import logging

class logger:
  #KEEPSEYE ON WARNING LEVEL LOGS
  logger = logging.getLogger('discord')
  logger.setLevel(logging.WARNING)
  handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
  handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
  logger.addHandler(handler)

  def run():
    logger()