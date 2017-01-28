

#calss header
class _PROMPT():
	def __init__(self,): 
		self.name = "PROMPT"
		self.definitions = [u'(of an action) done quickly and without delay, or (of a person) acting quickly or arriving at the arranged time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
