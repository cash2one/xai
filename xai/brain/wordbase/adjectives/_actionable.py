

#calss header
class _ACTIONABLE():
	def __init__(self,): 
		self.name = "ACTIONABLE"
		self.definitions = [u'If something is actionable, it gives someone a good reason for accusing someone in a law court: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
