

#calss header
class _UNJUSTIFIED():
	def __init__(self,): 
		self.name = "UNJUSTIFIED"
		self.definitions = [u'wrong and/or not deserved: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
