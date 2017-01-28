

#calss header
class _RENEWABLE():
	def __init__(self,): 
		self.name = "RENEWABLE"
		self.definitions = [u'Renewable forms of energy can be produced as quickly as they are used: ', u'If an official document is renewable, its use can be continued for an extra period of time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
