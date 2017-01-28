

#calss header
class _CANKERED():
	def __init__(self,): 
		self.name = "CANKERED"
		self.definitions = [u'a cankered tree or fruit is affected by the canker disease: ', u'evil, unhealthy, or decayed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
