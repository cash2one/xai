

#calss header
class _CONTENTED():
	def __init__(self,): 
		self.name = "CONTENTED"
		self.definitions = [u'happy and satisfied: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
