

#calss header
class _UNDESIRABLE():
	def __init__(self,): 
		self.name = "UNDESIRABLE"
		self.definitions = [u'not wanted, approved of, or popular: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
