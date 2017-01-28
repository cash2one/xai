

#calss header
class _DILAPIDATED():
	def __init__(self,): 
		self.name = "DILAPIDATED"
		self.definitions = [u'old and in poor condition: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
