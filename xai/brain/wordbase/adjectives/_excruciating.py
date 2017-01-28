

#calss header
class _EXCRUCIATING():
	def __init__(self,): 
		self.name = "EXCRUCIATING"
		self.definitions = [u'extremely painful: ', u'extremely boring or embarrassing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
