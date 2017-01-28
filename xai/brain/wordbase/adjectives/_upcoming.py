

#calss header
class _UPCOMING():
	def __init__(self,): 
		self.name = "UPCOMING"
		self.definitions = [u'happening soon: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
