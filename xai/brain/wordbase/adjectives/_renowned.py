

#calss header
class _RENOWNED():
	def __init__(self,): 
		self.name = "RENOWNED"
		self.definitions = [u'famous for something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
