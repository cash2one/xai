

#calss header
class _ONSHORE():
	def __init__(self,): 
		self.name = "ONSHORE"
		self.definitions = [u'moving towards land from the sea, or on land rather than at sea: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
