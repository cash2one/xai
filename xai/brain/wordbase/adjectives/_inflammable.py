

#calss header
class _INFLAMMABLE():
	def __init__(self,): 
		self.name = "INFLAMMABLE"
		self.definitions = [u'An inflammable substance or material burns very easily: ', u'likely to become violent or angry very quickly and in an uncontrolled way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
