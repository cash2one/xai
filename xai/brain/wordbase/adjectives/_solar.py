

#calss header
class _SOLAR():
	def __init__(self,): 
		self.name = "SOLAR"
		self.definitions = [u'of or from the sun, or using the energy from the sun to produce electric power: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
