

#calss header
class _BULLETPROOF():
	def __init__(self,): 
		self.name = "BULLETPROOF"
		self.definitions = [u'Something that is bulletproof prevents bullets from going through it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
