

#calss header
class _ARGUABLY():
	def __init__(self,): 
		self.name = "ARGUABLY"
		self.definitions = [u'used when stating an opinion or belief that you think can be shown to be true: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
