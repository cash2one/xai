

#calss header
class _FRISKY():
	def __init__(self,): 
		self.name = "FRISKY"
		self.definitions = [u'(of a person or an animal) liking to play or full of activity: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
