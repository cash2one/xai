

#calss header
class _BARBED():
	def __init__(self,): 
		self.name = "BARBED"
		self.definitions = [u'having a sharp point that curves backwards', u'unkind and criticizing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
