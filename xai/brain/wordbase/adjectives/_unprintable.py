

#calss header
class _UNPRINTABLE():
	def __init__(self,): 
		self.name = "UNPRINTABLE"
		self.definitions = [u'containing offensive language and therefore not acceptable in printed form, for example in a newspaper: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
