

#calss header
class _POOR():
	def __init__(self,): 
		self.name = "POOR"
		self.definitions = [u'having little money and/or few possessions: ', u'to have very little of a particular substance or quality: ', u'not good; being of a very low quality, quantity, or standard: ', u'deserving sympathy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
