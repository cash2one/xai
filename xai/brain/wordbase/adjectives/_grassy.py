

#calss header
class _GRASSY():
	def __init__(self,): 
		self.name = "GRASSY"
		self.definitions = [u'covered with grass: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
