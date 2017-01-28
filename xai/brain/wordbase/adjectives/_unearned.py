

#calss header
class _UNEARNED():
	def __init__(self,): 
		self.name = "UNEARNED"
		self.definitions = [u'earned or obtained without having been worked for: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
