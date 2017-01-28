

#calss header
class _LAMENTABLE():
	def __init__(self,): 
		self.name = "LAMENTABLE"
		self.definitions = [u'deserving severe criticism; very bad: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
