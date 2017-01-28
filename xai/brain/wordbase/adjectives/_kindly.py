

#calss header
class _KINDLY():
	def __init__(self,): 
		self.name = "KINDLY"
		self.definitions = [u'A kindly person or action is a kind one: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
