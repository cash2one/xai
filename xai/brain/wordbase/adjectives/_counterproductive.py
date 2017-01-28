

#calss header
class _COUNTERPRODUCTIVE():
	def __init__(self,): 
		self.name = "COUNTERPRODUCTIVE"
		self.definitions = [u'having an effect that is opposite to the one intended or wanted: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
