

#calss header
class _SOPHOMORIC():
	def __init__(self,): 
		self.name = "SOPHOMORIC"
		self.definitions = [u'silly and behaving like a child: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
