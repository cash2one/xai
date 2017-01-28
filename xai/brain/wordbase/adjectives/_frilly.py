

#calss header
class _FRILLY():
	def __init__(self,): 
		self.name = "FRILLY"
		self.definitions = [u'with a lot of frills: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
