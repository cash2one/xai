

#calss header
class _DECIDUOUS():
	def __init__(self,): 
		self.name = "DECIDUOUS"
		self.definitions = [u'A deciduous tree loses its leaves in autumn and grows new ones in the spring.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
