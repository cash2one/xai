

#calss header
class _GRAND():
	def __init__(self,): 
		self.name = "GRAND"
		self.definitions = [u'important and large in degree: ', u'impressive and large or important: ', u'used in the name of a place or building to show that it is large or beautiful and deserves to be admired: ', u'excellent or enjoyable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
