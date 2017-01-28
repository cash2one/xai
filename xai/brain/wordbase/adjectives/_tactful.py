

#calss header
class _TACTFUL():
	def __init__(self,): 
		self.name = "TACTFUL"
		self.definitions = [u'careful not to say or do anything that could upset someone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
