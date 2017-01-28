

#calss header
class _LUCID():
	def __init__(self,): 
		self.name = "LUCID"
		self.definitions = [u'clearly expressed and easy to understand, or (of a person) thinking or speaking clearly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
