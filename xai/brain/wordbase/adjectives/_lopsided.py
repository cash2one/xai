

#calss header
class _LOPSIDED():
	def __init__(self,): 
		self.name = "LOPSIDED"
		self.definitions = [u'with one side bigger, higher, etc. than the other; not equally balanced: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
