

#calss header
class _AWRY():
	def __init__(self,): 
		self.name = "AWRY"
		self.definitions = [u'not in the intended way: ', u'in the wrong position: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
