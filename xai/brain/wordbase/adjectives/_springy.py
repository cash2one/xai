

#calss header
class _SPRINGY():
	def __init__(self,): 
		self.name = "SPRINGY"
		self.definitions = [u'returning quickly to the usual shape, after being pulled, pushed, crushed, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
