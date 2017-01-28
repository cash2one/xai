

#calss header
class _STRONGLY():
	def __init__(self,): 
		self.name = "STRONGLY"
		self.definitions = [u'very much or in a very serious way: ', u'in a way or form that is difficult to break: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
