

#calss header
class _MASS():
	def __init__(self,): 
		self.name = "MASS"
		self.definitions = [u'having an effect on or involving a large number of people or forming a large amount: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
