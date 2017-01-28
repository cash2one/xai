

#calss header
class _VAIN():
	def __init__(self,): 
		self.name = "VAIN"
		self.definitions = [u'unsuccessful; of no value: ', u'unsuccessfully: ', u'too interested in your own appearance or achievements: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
