

#calss header
class _WITHERED():
	def __init__(self,): 
		self.name = "WITHERED"
		self.definitions = [u'dry and decaying: ', u'A withered arm or leg has not grown to its correct size because of disease.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
