

#calss header
class _IMPORTUNATE():
	def __init__(self,): 
		self.name = "IMPORTUNATE"
		self.definitions = [u'repeatedly asking for something, in a forceful and annoying way: ', u'An importunate request or question is repeated and forceful in an annoying way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
