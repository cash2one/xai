

#calss header
class _FLESHLY():
	def __init__(self,): 
		self.name = "FLESHLY"
		self.definitions = [u'relating to the physical body, not the mind or the soul: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
