

#calss header
class _DIFFUSE():
	def __init__(self,): 
		self.name = "DIFFUSE"
		self.definitions = [u'spread out and not directed in one place: ', u'not clear or easy to understand: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
