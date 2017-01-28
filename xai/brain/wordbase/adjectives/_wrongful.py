

#calss header
class _WRONGFUL():
	def __init__(self,): 
		self.name = "WRONGFUL"
		self.definitions = [u'Wrongful actions are unfair or illegal: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
