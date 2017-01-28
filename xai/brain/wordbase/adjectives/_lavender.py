

#calss header
class _LAVENDER():
	def __init__(self,): 
		self.name = "LAVENDER"
		self.definitions = [u'of a pale purple colour']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
