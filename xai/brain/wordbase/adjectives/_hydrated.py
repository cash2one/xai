

#calss header
class _HYDRATED():
	def __init__(self,): 
		self.name = "HYDRATED"
		self.definitions = [u'having absorbed enough water or other liquid: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
