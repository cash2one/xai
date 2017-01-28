

#calss header
class _SHAG():
	def __init__(self,): 
		self.name = "SHAG"
		self.definitions = [u'(of a carpet) made of long thick threads: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
