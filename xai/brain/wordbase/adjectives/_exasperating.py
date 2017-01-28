

#calss header
class _EXASPERATING():
	def __init__(self,): 
		self.name = "EXASPERATING"
		self.definitions = [u'annoying, especially because you can do nothing to solve a problem: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
