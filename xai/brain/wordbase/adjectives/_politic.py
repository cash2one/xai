

#calss header
class _POLITIC():
	def __init__(self,): 
		self.name = "POLITIC"
		self.definitions = [u'wise and showing the ability to make the right decisions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
