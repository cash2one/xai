

#calss header
class _INTERDEPENDENT():
	def __init__(self,): 
		self.name = "INTERDEPENDENT"
		self.definitions = [u'depending on each other: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
