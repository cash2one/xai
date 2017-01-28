

#calss header
class _PASTORAL():
	def __init__(self,): 
		self.name = "PASTORAL"
		self.definitions = [u'used to refer to the part of the work of teachers and priests that involves giving help and advice about personal matters: ', u'A pastoral piece of art, writing, or music represents the pleasant and traditional features of the countryside: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
