

#calss header
class _GLAMOROUS():
	def __init__(self,): 
		self.name = "GLAMOROUS"
		self.definitions = [u'attractive in an exciting and special way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
