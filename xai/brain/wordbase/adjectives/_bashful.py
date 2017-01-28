

#calss header
class _BASHFUL():
	def __init__(self,): 
		self.name = "BASHFUL"
		self.definitions = [u'often feeling uncomfortable with other people and easily embarrassed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
