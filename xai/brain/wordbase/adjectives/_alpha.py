

#calss header
class _ALPHA():
	def __init__(self,): 
		self.name = "ALPHA"
		self.definitions = [u'Alpha software is at the first stage of development: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
