

#calss header
class _PENETRATIVE():
	def __init__(self,): 
		self.name = "PENETRATIVE"
		self.definitions = [u'involving movement into or through something or someone: ', u'showing understanding: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
