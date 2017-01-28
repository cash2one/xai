

#calss header
class _OPTICAL():
	def __init__(self,): 
		self.name = "OPTICAL"
		self.definitions = [u'relating to light or the ability to see: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
