

#calss header
class _VANISHING():
	def __init__(self,): 
		self.name = "VANISHING"
		self.definitions = [u'beginning to disappear: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
