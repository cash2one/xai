

#calss header
class _DISPROPORTIONATE():
	def __init__(self,): 
		self.name = "DISPROPORTIONATE"
		self.definitions = [u'too large or too small in comparison to something else, or not deserving its importance or influence: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
