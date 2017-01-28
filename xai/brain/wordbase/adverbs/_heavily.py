

#calss header
class _HEAVILY():
	def __init__(self,): 
		self.name = "HEAVILY"
		self.definitions = [u'to a great degree: ', u'with force, or in a way that needs a lot of effort to move or lift: ', u'in a way that is difficult to accept or deal with: ', u'in a strong, thick, or solid way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
