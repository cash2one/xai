

#calss header
class _FOREVER():
	def __init__(self,): 
		self.name = "FOREVER"
		self.definitions = [u'for all time: ', u'for an extremely long time or too much time: ', u'very often: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
