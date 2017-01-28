

#calss header
class _TAXABLE():
	def __init__(self,): 
		self.name = "TAXABLE"
		self.definitions = [u'If something is taxable, you must pay tax on it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
