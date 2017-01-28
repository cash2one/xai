

#calss header
class _HYDROELECTRIC():
	def __init__(self,): 
		self.name = "HYDROELECTRIC"
		self.definitions = [u'producing electricity by the force of fast moving water such as rivers or waterfalls: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
