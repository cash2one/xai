

#calss header
class _IRREPROACHABLE():
	def __init__(self,): 
		self.name = "IRREPROACHABLE"
		self.definitions = [u'without fault and therefore impossible to criticize: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
