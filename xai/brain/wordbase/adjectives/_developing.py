

#calss header
class _DEVELOPING():
	def __init__(self,): 
		self.name = "DEVELOPING"
		self.definitions = [u'A developing country or area of the world is poorer and has less advanced industries, especially in Africa, Latin America, or Asia: ', u'growing or becoming stronger or more advanced']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
