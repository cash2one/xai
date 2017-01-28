

#calss header
class _SOUTHWEST():
	def __init__(self,): 
		self.name = "SOUTHWEST"
		self.definitions = [u'in or towards the southwest: ', u'a wind that comes from the southwest']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
