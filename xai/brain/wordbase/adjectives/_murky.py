

#calss header
class _MURKY():
	def __init__(self,): 
		self.name = "MURKY"
		self.definitions = [u'dark and dirty or difficult to see through: ', u'used to describe a situation that is complicated and unpleasant, and about which many facts are not clear: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
