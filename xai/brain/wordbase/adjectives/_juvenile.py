

#calss header
class _JUVENILE():
	def __init__(self,): 
		self.name = "JUVENILE"
		self.definitions = [u'relating to a young person who is not yet old enough to be considered an adult: ', u'silly and typical of a child: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
