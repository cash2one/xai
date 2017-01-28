

#calss header
class _INTACT():
	def __init__(self,): 
		self.name = "INTACT"
		self.definitions = [u'complete and in the original state: ', u'not damaged: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
