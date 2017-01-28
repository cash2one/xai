

#calss header
class _MEDIEVAL():
	def __init__(self,): 
		self.name = "MEDIEVAL"
		self.definitions = [u'related to the Middle Ages (= the period in European history from about AD 600 to AD 1500): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
