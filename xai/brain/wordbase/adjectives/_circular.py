

#calss header
class _CIRCULAR():
	def __init__(self,): 
		self.name = "CIRCULAR"
		self.definitions = [u'shaped like a circle: ', u'A circular argument is one that keeps returning to the same points and is not effective.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
