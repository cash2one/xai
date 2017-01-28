

#calss header
class _REPUTED():
	def __init__(self,): 
		self.name = "REPUTED"
		self.definitions = [u'said to be the true situation although this is not known to be certain and may not be likely: ', u'famous and with a good reputation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
