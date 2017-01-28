

#calss header
class _MUCKY():
	def __init__(self,): 
		self.name = "MUCKY"
		self.definitions = [u'dirty: ', u'related to or describing sex in an offensive way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
