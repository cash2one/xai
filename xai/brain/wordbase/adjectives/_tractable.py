

#calss header
class _TRACTABLE():
	def __init__(self,): 
		self.name = "TRACTABLE"
		self.definitions = [u'easily dealt with, controlled, or persuaded: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
