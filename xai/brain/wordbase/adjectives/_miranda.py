

#calss header
class _MIRANDA():
	def __init__(self,): 
		self.name = "MIRANDA"
		self.definitions = [u'involving warnings that police must give to people they arrest, so that people do not say something that will harm them later in court: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
