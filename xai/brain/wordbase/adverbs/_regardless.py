

#calss header
class _REGARDLESS():
	def __init__(self,): 
		self.name = "REGARDLESS"
		self.definitions = [u'despite; not being affected by something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
