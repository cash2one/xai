

#calss header
class _FORBEARING():
	def __init__(self,): 
		self.name = "FORBEARING"
		self.definitions = [u'patient and forgiving: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
