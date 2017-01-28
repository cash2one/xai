

#calss header
class _CENTRIST():
	def __init__(self,): 
		self.name = "CENTRIST"
		self.definitions = [u'supporting the centre of the range of political opinions']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
