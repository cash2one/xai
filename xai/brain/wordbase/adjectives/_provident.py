

#calss header
class _PROVIDENT():
	def __init__(self,): 
		self.name = "PROVIDENT"
		self.definitions = [u'making arrangements for future needs, especially by saving money']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
