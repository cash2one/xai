

#calss header
class _PROMOTIONAL():
	def __init__(self,): 
		self.name = "PROMOTIONAL"
		self.definitions = [u'intended to advertise something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
