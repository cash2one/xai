

#calss header
class _VARIEGATED():
	def __init__(self,): 
		self.name = "VARIEGATED"
		self.definitions = [u'having a pattern of different colours or marks: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
