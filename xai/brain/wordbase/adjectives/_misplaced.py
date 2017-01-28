

#calss header
class _MISPLACED():
	def __init__(self,): 
		self.name = "MISPLACED"
		self.definitions = [u'directed towards someone or something wrongly or in a way that does not show good judgment: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
