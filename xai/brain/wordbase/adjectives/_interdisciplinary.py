

#calss header
class _INTERDISCIPLINARY():
	def __init__(self,): 
		self.name = "INTERDISCIPLINARY"
		self.definitions = [u'involving two or more different subjects or areas of knowledge: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
