

#calss header
class _SOLITARY():
	def __init__(self,): 
		self.name = "SOLITARY"
		self.definitions = [u'A solitary person or thing is the only person or thing in a place: ', u'done alone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
