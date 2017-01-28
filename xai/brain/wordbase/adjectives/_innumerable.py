

#calss header
class _INNUMERABLE():
	def __init__(self,): 
		self.name = "INNUMERABLE"
		self.definitions = [u'too many to be counted: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
