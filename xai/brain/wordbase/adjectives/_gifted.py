

#calss header
class _GIFTED():
	def __init__(self,): 
		self.name = "GIFTED"
		self.definitions = [u'having special ability in a particular subject or activity: ', u'clever, or having a special ability: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
