

#calss header
class _GILT():
	def __init__(self,): 
		self.name = "GILT"
		self.definitions = [u'covered with a thin layer of gold or a substance that is intended to look like it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
