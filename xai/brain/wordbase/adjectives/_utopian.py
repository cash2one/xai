

#calss header
class _UTOPIAN():
	def __init__(self,): 
		self.name = "UTOPIAN"
		self.definitions = [u'relating to or aiming for a perfect society in which everyone works well with each other and is happy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
