

#calss header
class _GRISLY():
	def __init__(self,): 
		self.name = "GRISLY"
		self.definitions = [u'extremely unpleasant, especially because death or blood is involved: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
