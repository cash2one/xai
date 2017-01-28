

#calss header
class _OUTSIDE():
	def __init__(self,): 
		self.name = "OUTSIDE"
		self.definitions = [u'not in a particular building or room, but near it: ', u'not in a particular place: ', u'not within or part of something: ', u'except for: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
