

#calss header
class _WINNING():
	def __init__(self,): 
		self.name = "WINNING"
		self.definitions = [u'that has won something: ', u'friendly and charming and often making people like you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
