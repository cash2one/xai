

#calss header
class _RETALIATORY():
	def __init__(self,): 
		self.name = "RETALIATORY"
		self.definitions = [u'A retaliatory action is one that is harmful to someone who has done something to harm you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
