

#calss header
class _MARTYRED():
	def __init__(self,): 
		self.name = "MARTYRED"
		self.definitions = [u'A martyred person has been killed because of their religious or political beliefs: ', u'showing that you are suffering so that people will have sympathy for you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
