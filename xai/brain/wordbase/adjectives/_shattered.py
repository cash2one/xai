

#calss header
class _SHATTERED():
	def __init__(self,): 
		self.name = "SHATTERED"
		self.definitions = [u'broken into very small pieces: ', u'extremely upset: ', u'extremely tired: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
