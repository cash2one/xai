

#calss header
class _KINETIC():
	def __init__(self,): 
		self.name = "KINETIC"
		self.definitions = [u'involving or producing movement: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
