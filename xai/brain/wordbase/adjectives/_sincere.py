

#calss header
class _SINCERE():
	def __init__(self,): 
		self.name = "SINCERE"
		self.definitions = [u'(of a person, feelings, or behaviour) not pretending or lying; honest: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
