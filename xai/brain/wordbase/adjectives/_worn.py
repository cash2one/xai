

#calss header
class _WORN():
	def __init__(self,): 
		self.name = "WORN"
		self.definitions = [u'damaged because of continuous use: ', u'very tired, and seeming old : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
