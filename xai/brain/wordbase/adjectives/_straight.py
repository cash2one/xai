

#calss header
class _STRAIGHT():
	def __init__(self,): 
		self.name = "STRAIGHT"
		self.definitions = [u'continuing in one direction without bending or curving: ', u'honest: ', u'If you tell someone something straight out, you say it directly and honestly, without trying to make what you are saying more pleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
