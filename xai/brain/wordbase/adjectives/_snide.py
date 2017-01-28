

#calss header
class _SNIDE():
	def __init__(self,): 
		self.name = "SNIDE"
		self.definitions = [u'(especially of remarks) containing unpleasant criticism that is not clearly stated: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
