

#calss header
class _DESOLATE():
	def __init__(self,): 
		self.name = "DESOLATE"
		self.definitions = [u'A desolate place is empty and not attractive, with no people or nothing pleasant in it: ', u'extremely sad and feeling alone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
