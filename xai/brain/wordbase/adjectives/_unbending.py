

#calss header
class _UNBENDING():
	def __init__(self,): 
		self.name = "UNBENDING"
		self.definitions = [u'If someone is unbending, they often make fixed judgments and decisions that they are unwilling to change: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
