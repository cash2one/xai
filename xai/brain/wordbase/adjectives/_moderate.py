

#calss header
class _MODERATE():
	def __init__(self,): 
		self.name = "MODERATE"
		self.definitions = [u'neither small nor large in size, amount, degree, or strength: ', u'Moderate opinions, especially political ones, are not extreme and are therefore acceptable to a large number of people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
