

#calss header
class _SEAFARING():
	def __init__(self,): 
		self.name = "SEAFARING"
		self.definitions = [u'connected with travelling by sea: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
