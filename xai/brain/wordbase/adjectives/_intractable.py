

#calss header
class _INTRACTABLE():
	def __init__(self,): 
		self.name = "INTRACTABLE"
		self.definitions = [u'very difficult or impossible to control, manage, or solve: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
