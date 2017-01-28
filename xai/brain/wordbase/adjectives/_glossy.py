

#calss header
class _GLOSSY():
	def __init__(self,): 
		self.name = "GLOSSY"
		self.definitions = [u'smooth and shiny: ', u'A glossy book or magazine has been produced on shiny and expensive paper and contains many colour pictures: ', u'looking attractive, but often not having serious value or quality: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
