

#calss header
class _SUPERHUMAN():
	def __init__(self,): 
		self.name = "SUPERHUMAN"
		self.definitions = [u'having more powers than, or seeming outside the powers of, a human: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
