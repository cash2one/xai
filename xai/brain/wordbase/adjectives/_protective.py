

#calss header
class _PROTECTIVE():
	def __init__(self,): 
		self.name = "PROTECTIVE"
		self.definitions = [u'giving protection: ', u'wanting to protect someone from criticism, hurt, danger, etc. because you like them very much: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
