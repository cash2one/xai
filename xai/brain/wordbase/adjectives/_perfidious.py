

#calss header
class _PERFIDIOUS():
	def __init__(self,): 
		self.name = "PERFIDIOUS"
		self.definitions = [u'unable to be trusted, or showing no loyalty: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
