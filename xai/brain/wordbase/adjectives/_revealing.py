

#calss header
class _REVEALING():
	def __init__(self,): 
		self.name = "REVEALING"
		self.definitions = [u'Revealing clothes show more of the body than is usual: ', u'showing something that was not previously known or seen: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
