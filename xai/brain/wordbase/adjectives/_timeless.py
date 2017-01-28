

#calss header
class _TIMELESS():
	def __init__(self,): 
		self.name = "TIMELESS"
		self.definitions = [u'Something that is timeless does not change as the years go past: ', u'having a value that is not limited to a particular period but will last for ever: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
