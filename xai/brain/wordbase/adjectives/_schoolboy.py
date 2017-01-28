

#calss header
class _SCHOOLBOY():
	def __init__(self,): 
		self.name = "SCHOOLBOY"
		self.definitions = [u'like a child or at the time when someone was a child: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
