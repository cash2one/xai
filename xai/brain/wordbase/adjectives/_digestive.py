

#calss header
class _DIGESTIVE():
	def __init__(self,): 
		self.name = "DIGESTIVE"
		self.definitions = [u'relating to the digestion of food: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
