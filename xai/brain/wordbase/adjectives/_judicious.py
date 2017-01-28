

#calss header
class _JUDICIOUS():
	def __init__(self,): 
		self.name = "JUDICIOUS"
		self.definitions = [u'having or showing reason and good judgment in making decisions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
