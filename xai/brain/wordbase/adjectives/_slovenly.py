

#calss header
class _SLOVENLY():
	def __init__(self,): 
		self.name = "SLOVENLY"
		self.definitions = [u'untidy and dirty: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
