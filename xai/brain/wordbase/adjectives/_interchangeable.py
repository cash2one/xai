

#calss header
class _INTERCHANGEABLE():
	def __init__(self,): 
		self.name = "INTERCHANGEABLE"
		self.definitions = [u'able to be exchanged with each other without making any difference or without being noticed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
