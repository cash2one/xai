

#calss header
class _RAUCOUS():
	def __init__(self,): 
		self.name = "RAUCOUS"
		self.definitions = [u'loud and unpleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
