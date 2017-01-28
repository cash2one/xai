

#calss header
class _IMPALPABLE():
	def __init__(self,): 
		self.name = "IMPALPABLE"
		self.definitions = [u'difficult to feel or understand: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
