

#calss header
class _CIRCULATORY():
	def __init__(self,): 
		self.name = "CIRCULATORY"
		self.definitions = [u'relating to the system that moves blood through the body and that includes the heart, arteries, and veins']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
