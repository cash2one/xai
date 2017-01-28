

#calss header
class _SPRING():
	def __init__(self,): 
		self.name = "SPRING"
		self.definitions = [u'(of furniture) using springs (= curved pieces of metal) to give support']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
