

#calss header
class _SLOTTED():
	def __init__(self,): 
		self.name = "SLOTTED"
		self.definitions = [u'A slotted kitchen utensil or tool has long, narrow holes in it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
