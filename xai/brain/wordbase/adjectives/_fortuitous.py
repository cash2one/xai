

#calss header
class _FORTUITOUS():
	def __init__(self,): 
		self.name = "FORTUITOUS"
		self.definitions = [u'(of something that is to your advantage) not planned, happening by chance: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
