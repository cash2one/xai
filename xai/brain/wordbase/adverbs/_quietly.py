

#calss header
class _QUIETLY():
	def __init__(self,): 
		self.name = "QUIETLY"
		self.definitions = [u'without making much noise: ', u'in a way that is not obvious to other people because you do not say much: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
