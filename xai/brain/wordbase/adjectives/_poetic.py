

#calss header
class _POETIC():
	def __init__(self,): 
		self.name = "POETIC"
		self.definitions = [u'like or relating to poetry or poets: ', u'very beautiful or expressing emotion: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
