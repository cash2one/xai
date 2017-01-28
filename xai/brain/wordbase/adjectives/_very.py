

#calss header
class _VERY():
	def __init__(self,): 
		self.name = "VERY"
		self.definitions = [u'(used to add emphasis to a noun) exact or particular: ', u'used to describe or emphasize the furthest point of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
