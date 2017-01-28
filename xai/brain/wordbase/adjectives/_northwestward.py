

#calss header
class _NORTHWESTWARD():
	def __init__(self,): 
		self.name = "NORTHWESTWARD"
		self.definitions = [u'towards the northwest: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
