

#calss header
class _SPARKLING():
	def __init__(self,): 
		self.name = "SPARKLING"
		self.definitions = [u'shining brightly: ', u'energetic and interesting: ', u'A sparkling drink is one that contains many small bubbles of gas: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
