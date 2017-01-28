

#calss header
class _UNOCCUPIED():
	def __init__(self,): 
		self.name = "UNOCCUPIED"
		self.definitions = [u'without anyone in it, or not busy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
