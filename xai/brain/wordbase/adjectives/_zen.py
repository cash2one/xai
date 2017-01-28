

#calss header
class _ZEN():
	def __init__(self,): 
		self.name = "ZEN"
		self.definitions = [u'relaxed and not worrying about things that you cannot change: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
