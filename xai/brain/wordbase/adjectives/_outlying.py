

#calss header
class _OUTLYING():
	def __init__(self,): 
		self.name = "OUTLYING"
		self.definitions = [u'far away from main towns and cities, or far from the centre of a place: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
