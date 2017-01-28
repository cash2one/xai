

#calss header
class _CARNAL():
	def __init__(self,): 
		self.name = "CARNAL"
		self.definitions = [u'relating to the physical feelings and wants of the body: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
