

#calss header
class _PUTRID():
	def __init__(self,): 
		self.name = "PUTRID"
		self.definitions = [u'decayed and having an unpleasant smell: ', u'very unpleasant or ugly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
