

#calss header
class _TORTUOUS():
	def __init__(self,): 
		self.name = "TORTUOUS"
		self.definitions = [u'with many turns and changes of direction; not direct or simple: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
