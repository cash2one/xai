

#calss header
class _LET():
	def __init__(self,): 
		self.name = "LET"
		self.definitions = [u'used after a negative statement to emphasize how unlikely a situation is because something much more likely has never happened: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
