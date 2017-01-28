

#calss header
class _INARTICULATE():
	def __init__(self,): 
		self.name = "INARTICULATE"
		self.definitions = [u'unable to express feelings or ideas clearly, or expressed in a way that is difficult to understand: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
