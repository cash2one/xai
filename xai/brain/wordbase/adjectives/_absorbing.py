

#calss header
class _ABSORBING():
	def __init__(self,): 
		self.name = "ABSORBING"
		self.definitions = [u'Something that is absorbing is very interesting and keeps your attention: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
