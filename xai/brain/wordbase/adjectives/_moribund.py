

#calss header
class _MORIBUND():
	def __init__(self,): 
		self.name = "MORIBUND"
		self.definitions = [u'(especially of an organization or business) not active or successful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
