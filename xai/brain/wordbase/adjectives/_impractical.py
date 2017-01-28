

#calss header
class _IMPRACTICAL():
	def __init__(self,): 
		self.name = "IMPRACTICAL"
		self.definitions = [u'Impractical people are not naturally good at doing useful jobs such as making or repairing things.', u'Impractical arrangements, ideas, or methods cannot be done or used easily or effectively: ', u'Impractical clothes, devices, etc. cause problems when used in normal situations: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
