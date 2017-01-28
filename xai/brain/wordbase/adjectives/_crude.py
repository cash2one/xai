

#calss header
class _CRUDE():
	def __init__(self,): 
		self.name = "CRUDE"
		self.definitions = [u'simple and not skilfully done or made: ', u'rude and offensive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
