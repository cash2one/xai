

#calss header
class _FALLOW():
	def __init__(self,): 
		self.name = "FALLOW"
		self.definitions = [u'Fallow land is not planted with crops, in order to improve the quality of the soil: ', u'A fallow period of time is one in which very little happens: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
