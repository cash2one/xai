

#calss header
class _DISPENSABLE():
	def __init__(self,): 
		self.name = "DISPENSABLE"
		self.definitions = [u'more than you need and therefore not necessary; that can be got rid of: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
