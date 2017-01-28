

#calss header
class _BULLISH():
	def __init__(self,): 
		self.name = "BULLISH"
		self.definitions = [u'giving your opinions in a powerful and confident way: ', u'A bullish financial market is one in which share prices are rising.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
