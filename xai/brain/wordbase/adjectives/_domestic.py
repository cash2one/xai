

#calss header
class _DOMESTIC():
	def __init__(self,): 
		self.name = "DOMESTIC"
		self.definitions = [u"relating to a person's own country: ", u'belonging or relating to the home, house, or family: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
