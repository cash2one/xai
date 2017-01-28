

#calss header
class _SOCIABLE():
	def __init__(self,): 
		self.name = "SOCIABLE"
		self.definitions = [u'Sociable people like to meet and spend time with other people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
