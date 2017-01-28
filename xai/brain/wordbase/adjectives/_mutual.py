

#calss header
class _MUTUAL():
	def __init__(self,): 
		self.name = "MUTUAL"
		self.definitions = [u'(of two or more people or groups) feeling the same emotion, or doing the same thing to or for each other: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
