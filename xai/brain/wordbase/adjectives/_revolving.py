

#calss header
class _REVOLVING():
	def __init__(self,): 
		self.name = "REVOLVING"
		self.definitions = [u'used to refer to something that revolves (= moves around a central point): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
