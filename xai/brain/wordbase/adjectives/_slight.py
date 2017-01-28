

#calss header
class _SLIGHT():
	def __init__(self,): 
		self.name = "SLIGHT"
		self.definitions = [u'small in amount or degree: ', u'not at all: ', u'(of people) thin and delicate: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
