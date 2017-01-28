

#calss header
class _EXASPERATED():
	def __init__(self,): 
		self.name = "EXASPERATED"
		self.definitions = [u'annoyed, especially because you can do nothing to solve a problem: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
