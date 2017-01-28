

#calss header
class _CONJUGAL():
	def __init__(self,): 
		self.name = "CONJUGAL"
		self.definitions = [u'connected with marriage or the relationship between two married people, especially their sexual relationship: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
