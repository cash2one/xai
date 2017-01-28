

#calss header
class _WISE():
	def __init__(self,): 
		self.name = "WISE"
		self.definitions = [u'having or showing the ability to make good judgments, based on a deep understanding and experience of life: ', u'understanding a dishonest situation or way of doing something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
