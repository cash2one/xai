

#calss header
class _DEVOURING():
	def __init__(self,): 
		self.name = "DEVOURING"
		self.definitions = [u'a devouring emotion is extremely strong and usually causes damage: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
