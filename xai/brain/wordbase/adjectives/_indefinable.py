

#calss header
class _INDEFINABLE():
	def __init__(self,): 
		self.name = "INDEFINABLE"
		self.definitions = [u'impossible to clearly describe or explain: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
