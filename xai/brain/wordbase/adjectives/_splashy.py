

#calss header
class _SPLASHY():
	def __init__(self,): 
		self.name = "SPLASHY"
		self.definitions = [u'more expensive, exciting, etc. than necessary: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
