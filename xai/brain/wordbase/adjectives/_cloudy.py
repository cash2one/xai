

#calss header
class _CLOUDY():
	def __init__(self,): 
		self.name = "CLOUDY"
		self.definitions = [u'with clouds: ', u'not transparent: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
