

#calss header
class _EXPEDITIONARY():
	def __init__(self,): 
		self.name = "EXPEDITIONARY"
		self.definitions = [u'a group of soldiers sent to another country to fight in a war']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
