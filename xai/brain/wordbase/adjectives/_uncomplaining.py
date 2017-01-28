

#calss header
class _UNCOMPLAINING():
	def __init__(self,): 
		self.name = "UNCOMPLAINING"
		self.definitions = [u'willing to do boring or difficult work without complaining or becoming angry: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
