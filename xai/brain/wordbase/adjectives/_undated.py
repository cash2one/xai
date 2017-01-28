

#calss header
class _UNDATED():
	def __init__(self,): 
		self.name = "UNDATED"
		self.definitions = [u'An undated document has no date on it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
