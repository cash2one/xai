

#calss header
class _SHELTERED():
	def __init__(self,): 
		self.name = "SHELTERED"
		self.definitions = [u'protected from wind, rain, or other bad weather: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
