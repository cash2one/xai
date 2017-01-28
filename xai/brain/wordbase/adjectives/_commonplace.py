

#calss header
class _COMMONPLACE():
	def __init__(self,): 
		self.name = "COMMONPLACE"
		self.definitions = [u'happening often or often seen or experienced and so not considered to be special: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
