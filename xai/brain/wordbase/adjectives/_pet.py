

#calss header
class _PET():
	def __init__(self,): 
		self.name = "PET"
		self.definitions = [u'a theory, subject, hate, etc. that is special and important to you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
