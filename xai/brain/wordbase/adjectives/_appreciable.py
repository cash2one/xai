

#calss header
class _APPRECIABLE():
	def __init__(self,): 
		self.name = "APPRECIABLE"
		self.definitions = [u'If an amount or change is appreciable, it is large or noticeable enough to have an important effect: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
