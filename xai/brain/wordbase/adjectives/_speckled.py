

#calss header
class _SPECKLED():
	def __init__(self,): 
		self.name = "SPECKLED"
		self.definitions = [u'covered with speckles: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
