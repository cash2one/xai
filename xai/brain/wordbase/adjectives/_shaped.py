

#calss header
class _SHAPED():
	def __init__(self,): 
		self.name = "SHAPED"
		self.definitions = [u'having a particular shape: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
