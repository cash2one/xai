

#calss header
class _PERKY():
	def __init__(self,): 
		self.name = "PERKY"
		self.definitions = [u'happy and full of energy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
