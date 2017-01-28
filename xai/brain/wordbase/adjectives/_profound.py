

#calss header
class _PROFOUND():
	def __init__(self,): 
		self.name = "PROFOUND"
		self.definitions = [u'felt or experienced very strongly or in an extreme way: ', u'showing a clear and deep understanding of serious matters: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
