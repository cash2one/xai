

#calss header
class _CONTRITE():
	def __init__(self,): 
		self.name = "CONTRITE"
		self.definitions = [u'feeling very sorry and guilty for something bad that you have done: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
