

#calss header
class _SATISFYING():
	def __init__(self,): 
		self.name = "SATISFYING"
		self.definitions = [u'making you feel pleased by providing what you need or want: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
