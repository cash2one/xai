

#calss header
class _ALWAYS():
	def __init__(self,): 
		self.name = "ALWAYS"
		self.definitions = [u'every time or all the time: ', u'for ever: ', u'at all times in the past: ', u'used with "can" or "could" to suggest another possibility: ', u'again and again, usually in an annoying way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
