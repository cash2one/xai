

#calss header
class _LIMITING():
	def __init__(self,): 
		self.name = "LIMITING"
		self.definitions = [u'preventing you from having much choice: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
