

#calss header
class _PROMINENT():
	def __init__(self,): 
		self.name = "PROMINENT"
		self.definitions = [u'very well known and important: ', u'sticking out from a surface: ', u'Something that is in a prominent position can easily be seen: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
