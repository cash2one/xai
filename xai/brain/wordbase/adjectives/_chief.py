

#calss header
class _CHIEF():
	def __init__(self,): 
		self.name = "CHIEF"
		self.definitions = [u'most important or main: ', u'highest in rank: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
