

#calss header
class _ELASTIC():
	def __init__(self,): 
		self.name = "ELASTIC"
		self.definitions = [u'An elastic material is able to stretch and be returned to its original shape or size: ', u'able or likely to be changed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
