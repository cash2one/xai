

#calss header
class _TEMPERAMENTAL():
	def __init__(self,): 
		self.name = "TEMPERAMENTAL"
		self.definitions = [u'A tempermental person is someone whose mood often changes very suddenly: ', u'caused by your own character and feelings: ', u'A temperamental machine sometimes works and sometimes does not: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
