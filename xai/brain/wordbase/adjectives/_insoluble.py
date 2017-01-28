

#calss header
class _INSOLUBLE():
	def __init__(self,): 
		self.name = "INSOLUBLE"
		self.definitions = [u'(of a problem) so difficult that it is impossible to solve: ', u'(of a substance) impossible to dissolve: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
