

#calss header
class _JUDGMENTAL():
	def __init__(self,): 
		self.name = "JUDGMENTAL"
		self.definitions = [u'too quick to criticize people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
