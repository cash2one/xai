

#calss header
class _IRRESPONSIBLE():
	def __init__(self,): 
		self.name = "IRRESPONSIBLE"
		self.definitions = [u'not thinking enough or not worrying about the possible results of what you do: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
