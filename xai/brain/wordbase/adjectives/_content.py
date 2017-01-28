

#calss header
class _CONTENT():
	def __init__(self,): 
		self.name = "CONTENT"
		self.definitions = [u'pleased with your situation and not hoping for change or improvement: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
