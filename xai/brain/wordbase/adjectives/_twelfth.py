

#calss header
class _TWELFTH():
	def __init__(self,): 
		self.name = "TWELFTH"
		self.definitions = [u'12th written as a word: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
