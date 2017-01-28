

#calss header
class _UNSURE():
	def __init__(self,): 
		self.name = "UNSURE"
		self.definitions = [u'not certain or having doubts: ', u'without confidence in yourself: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
