

#calss header
class _HASTY():
	def __init__(self,): 
		self.name = "HASTY"
		self.definitions = [u'Hasty actions are done in a hurry, sometimes without the necessary care or thought: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
