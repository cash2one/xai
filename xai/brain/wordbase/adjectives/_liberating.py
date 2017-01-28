

#calss header
class _LIBERATING():
	def __init__(self,): 
		self.name = "LIBERATING"
		self.definitions = [u'making you feel free and able to behave as you like: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
