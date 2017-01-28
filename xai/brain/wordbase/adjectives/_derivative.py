

#calss header
class _DERIVATIVE():
	def __init__(self,): 
		self.name = "DERIVATIVE"
		self.definitions = [u'If something is derivative, it is not the result of new ideas, but has been developed from or copies something else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
