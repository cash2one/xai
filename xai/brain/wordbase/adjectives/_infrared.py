

#calss header
class _INFRARED():
	def __init__(self,): 
		self.name = "INFRARED"
		self.definitions = [u'Infrared light is a type of light that feels warm but cannot be seen: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
