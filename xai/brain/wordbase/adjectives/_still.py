

#calss header
class _STILL():
	def __init__(self,): 
		self.name = "STILL"
		self.definitions = [u'staying in the same position; not moving: ', u'A still drink is one that is not fizzy (= with bubbles): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
