

#calss header
class _HORRID():
	def __init__(self,): 
		self.name = "HORRID"
		self.definitions = [u'unpleasant or unkind: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
