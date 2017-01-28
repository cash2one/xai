

#calss header
class _AMOK():
	def __init__(self,): 
		self.name = "AMOK"
		self.definitions = [u'to be out of control and act in a wild or dangerous manner: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
