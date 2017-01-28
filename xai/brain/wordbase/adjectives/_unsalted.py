

#calss header
class _UNSALTED():
	def __init__(self,): 
		self.name = "UNSALTED"
		self.definitions = [u'with no salt added: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
