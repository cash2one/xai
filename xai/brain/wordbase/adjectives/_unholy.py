

#calss header
class _UNHOLY():
	def __init__(self,): 
		self.name = "UNHOLY"
		self.definitions = [u'used to describe a combination of things when it is very bad, harmful, or unpleasant: ', u'extremely unpleasant: ', u'not pure or religious: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
