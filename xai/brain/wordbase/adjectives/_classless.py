

#calss header
class _CLASSLESS():
	def __init__(self,): 
		self.name = "CLASSLESS"
		self.definitions = [u'not belonging to a particular social class: ', u'having no different social classes: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
