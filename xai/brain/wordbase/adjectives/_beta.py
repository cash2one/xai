

#calss header
class _BETA():
	def __init__(self,): 
		self.name = "BETA"
		self.definitions = [u'Beta software is at the second stage of development: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
