

#calss header
class _CRABBY():
	def __init__(self,): 
		self.name = "CRABBY"
		self.definitions = [u'easily annoyed and complaining: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
