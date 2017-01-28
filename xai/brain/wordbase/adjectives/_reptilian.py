

#calss header
class _REPTILIAN():
	def __init__(self,): 
		self.name = "REPTILIAN"
		self.definitions = [u'belonging to or like a reptile: ', u'used to describe an unpleasantly strange and unfriendly person or type of behaviour: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
