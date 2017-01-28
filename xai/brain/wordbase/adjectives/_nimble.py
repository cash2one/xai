

#calss header
class _NIMBLE():
	def __init__(self,): 
		self.name = "NIMBLE"
		self.definitions = [u'quick and exact either in movement or thoughts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
