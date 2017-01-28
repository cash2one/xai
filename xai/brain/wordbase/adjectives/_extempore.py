

#calss header
class _EXTEMPORE():
	def __init__(self,): 
		self.name = "EXTEMPORE"
		self.definitions = [u'done or said without any preparation or thought: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
