

#calss header
class _MEANINGFUL():
	def __init__(self,): 
		self.name = "MEANINGFUL"
		self.definitions = [u'intended to show meaning, often secretly: ', u'useful, serious, or important: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
