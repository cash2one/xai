

#calss header
class _RUNNY():
	def __init__(self,): 
		self.name = "RUNNY"
		self.definitions = [u'more liquid than usual: ', u'If your nose is runny, it is producing more mucus than usual, usually because you are ill: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
