

#calss header
class _GUSHING():
	def __init__(self,): 
		self.name = "GUSHING"
		self.definitions = [u'expressing a positive feeling, especially praise, in such a strong way that it does not sound sincere: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
