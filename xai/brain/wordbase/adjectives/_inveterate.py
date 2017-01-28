

#calss header
class _INVETERATE():
	def __init__(self,): 
		self.name = "INVETERATE"
		self.definitions = [u'someone who does something very often and cannot stop doing it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
