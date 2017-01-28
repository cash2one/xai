

#calss header
class _PRINTABLE():
	def __init__(self,): 
		self.name = "PRINTABLE"
		self.definitions = [u'If something that is said is not printable, it is too rude or offensive to be included in a newspaper or magazine: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
