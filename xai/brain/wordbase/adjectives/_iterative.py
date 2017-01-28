

#calss header
class _ITERATIVE():
	def __init__(self,): 
		self.name = "ITERATIVE"
		self.definitions = [u'doing something again and again, usually to improve it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
