

#calss header
class _LAMBENT():
	def __init__(self,): 
		self.name = "LAMBENT"
		self.definitions = [u'shining gently: ', u'the ability to use words in a clever and humorous way without being unkind']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
