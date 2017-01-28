

#calss header
class _UNACCEPTABLY():
	def __init__(self,): 
		self.name = "UNACCEPTABLY"
		self.definitions = [u'in a way that cannot be accepted, approved of, or allowed to continue: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
