

#calss header
class _BLASPHEMOUS():
	def __init__(self,): 
		self.name = "BLASPHEMOUS"
		self.definitions = [u'considered offensive to God or religion: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
