

#calss header
class _PROFESSORIAL():
	def __init__(self,): 
		self.name = "PROFESSORIAL"
		self.definitions = [u'of or like a professor: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
