

#calss header
class _IMPROBABLE():
	def __init__(self,): 
		self.name = "IMPROBABLE"
		self.definitions = [u'not likely to happen or be true: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
