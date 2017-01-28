

#calss header
class _DEPARTED():
	def __init__(self,): 
		self.name = "DEPARTED"
		self.definitions = [u'dead: ', u'used to refer to something that happened in the past and is finished: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
