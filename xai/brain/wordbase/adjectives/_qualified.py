

#calss header
class _QUALIFIED():
	def __init__(self,): 
		self.name = "QUALIFIED"
		self.definitions = [u'having finished a training course, or having particular skills, etc.: ', u'limited: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
