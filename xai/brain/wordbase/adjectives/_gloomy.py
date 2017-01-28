

#calss header
class _GLOOMY():
	def __init__(self,): 
		self.name = "GLOOMY"
		self.definitions = [u'unhappy and without hope: ', u'not expecting or believing anything good in a situation: ', u'dark in a way that is unpleasant and makes it difficult to see: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
