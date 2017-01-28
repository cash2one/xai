

#calss header
class _RHOMBOID():
	def __init__(self,): 
		self.name = "RHOMBOID"
		self.definitions = [u'shaped like a rhomboid: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
