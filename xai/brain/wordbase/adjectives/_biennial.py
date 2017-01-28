

#calss header
class _BIENNIAL():
	def __init__(self,): 
		self.name = "BIENNIAL"
		self.definitions = [u'happening once every two years']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
