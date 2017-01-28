

#calss header
class _TEMPTING():
	def __init__(self,): 
		self.name = "TEMPTING"
		self.definitions = [u'If something is tempting, you want to do or have it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
