

#calss header
class _LOUD():
	def __init__(self,): 
		self.name = "LOUD"
		self.definitions = [u'making a lot of noise: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
