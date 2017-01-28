

#calss header
class _PILOT():
	def __init__(self,): 
		self.name = "PILOT"
		self.definitions = [u'A pilot plan, product, or system is used to test how good something is before introducing it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
