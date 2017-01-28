

#calss header
class _DECLAMATORY():
	def __init__(self,): 
		self.name = "DECLAMATORY"
		self.definitions = [u'expressing something with strong feeling, especially in a loud voice or with forceful language: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
