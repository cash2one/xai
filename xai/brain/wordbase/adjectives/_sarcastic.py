

#calss header
class _SARCASTIC():
	def __init__(self,): 
		self.name = "SARCASTIC"
		self.definitions = [u'using sarcasm: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
