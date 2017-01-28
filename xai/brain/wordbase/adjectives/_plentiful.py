

#calss header
class _PLENTIFUL():
	def __init__(self,): 
		self.name = "PLENTIFUL"
		self.definitions = [u'If something is plentiful, there is a lot of it available: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
