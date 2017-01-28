

#calss header
class _FAMILIAL():
	def __init__(self,): 
		self.name = "FAMILIAL"
		self.definitions = [u'similar to that in a family: ', u'affecting several members of the same family: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
