

#calss header
class _UNBALANCED():
	def __init__(self,): 
		self.name = "UNBALANCED"
		self.definitions = [u'not firm but likely to fall or change position suddenly', u'mentally ill: ', u'not fair or equal; false: ', u'not consisting of a combination of the correct types and amounts of food: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
