

#calss header
class _SUBJECTIVE():
	def __init__(self,): 
		self.name = "SUBJECTIVE"
		self.definitions = [u'influenced by or based on personal beliefs or feelings, rather than based on facts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
