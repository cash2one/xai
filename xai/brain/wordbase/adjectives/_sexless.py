

#calss header
class _SEXLESS():
	def __init__(self,): 
		self.name = "SEXLESS"
		self.definitions = [u'not being sexually attractive or not having an interest in sex: ', u'without sexual characteristics']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
