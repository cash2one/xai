

#calss header
class _BREAKABLE():
	def __init__(self,): 
		self.name = "BREAKABLE"
		self.definitions = [u'Something that is breakable might easily break: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
