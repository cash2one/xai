

#calss header
class _CROOKED():
	def __init__(self,): 
		self.name = "CROOKED"
		self.definitions = [u'not forming a straight line, or having many bends: ', u'dishonest: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
