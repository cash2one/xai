

#calss header
class _NAGGING():
	def __init__(self,): 
		self.name = "NAGGING"
		self.definitions = [u'complaining or criticizing: ', u'used to describe an unpleasant feeling that continues for a long period of time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
