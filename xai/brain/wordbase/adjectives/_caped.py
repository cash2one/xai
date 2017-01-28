

#calss header
class _CAPED():
	def __init__(self,): 
		self.name = "CAPED"
		self.definitions = [u'wearing a cape']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
