

#calss header
class _PRECOCIOUS():
	def __init__(self,): 
		self.name = "PRECOCIOUS"
		self.definitions = [u'(especially of children) showing mental development or achievement much earlier than usual: ', u'A precocious child behaves as if they are much older than they are: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
