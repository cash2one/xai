

#calss header
class _CUTTHROAT():
	def __init__(self,): 
		self.name = "CUTTHROAT"
		self.definitions = [u'not involving considering or worrying about any harm caused to others: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
