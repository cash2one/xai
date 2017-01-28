

#calss header
class _LITIGIOUS():
	def __init__(self,): 
		self.name = "LITIGIOUS"
		self.definitions = [u'too often taking arguments to a court of law for a decision: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
