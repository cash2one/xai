

#calss header
class _RUTTING():
	def __init__(self,): 
		self.name = "RUTTING"
		self.definitions = [u'relating to the period of the year during which particular male animals are sexually active: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
