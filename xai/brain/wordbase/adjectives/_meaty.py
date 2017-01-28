

#calss header
class _MEATY():
	def __init__(self,): 
		self.name = "MEATY"
		self.definitions = [u'full of meat or tasting a lot of meat: ', u'large and having a lot of flesh: ', u'having a lot of important or interesting ideas: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
