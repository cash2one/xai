

#calss header
class _RIVEN():
	def __init__(self,): 
		self.name = "RIVEN"
		self.definitions = [u'violently divided: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
