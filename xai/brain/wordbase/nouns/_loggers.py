

from xai.brain.wordbase.nouns._logger import _LOGGER

#calss header
class _LOGGERS(_LOGGER, ):
	def __init__(self,): 
		_LOGGER.__init__(self)
		self.name = "LOGGERS"
		self.specie = 'nouns'
		self.basic = "logger"
		self.jsondata = {}
