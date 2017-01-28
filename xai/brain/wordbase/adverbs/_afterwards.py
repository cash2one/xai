

#calss header
class _AFTERWARDS():
	def __init__(self,): 
		self.name = "AFTERWARDS"
		self.definitions = [u'after the time mentioned: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
