

#calss header
class _JUST():
	def __init__(self,): 
		self.name = "JUST"
		self.definitions = [u'fair; morally correct: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
