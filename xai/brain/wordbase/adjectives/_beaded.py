

#calss header
class _BEADED():
	def __init__(self,): 
		self.name = "BEADED"
		self.definitions = [u'decorated with beads: ', u'covered with small drops of sweat or a similar liquid: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
