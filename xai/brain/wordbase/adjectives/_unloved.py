

#calss header
class _UNLOVED():
	def __init__(self,): 
		self.name = "UNLOVED"
		self.definitions = [u'not loved: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
