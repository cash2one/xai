

#calss header
class _UNCARING():
	def __init__(self,): 
		self.name = "UNCARING"
		self.definitions = [u"not worrying about other people's troubles or doing anything to help them: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
