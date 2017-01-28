

#calss header
class _COEQUAL():
	def __init__(self,): 
		self.name = "COEQUAL"
		self.definitions = [u'equal in rank, ability, or power to another person or thing']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
