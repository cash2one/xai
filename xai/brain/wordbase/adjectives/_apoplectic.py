

#calss header
class _APOPLECTIC():
	def __init__(self,): 
		self.name = "APOPLECTIC"
		self.definitions = [u'extremely and obviously angry: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
