

#calss header
class _TROUBLING():
	def __init__(self,): 
		self.name = "TROUBLING"
		self.definitions = [u'Something that is troubling makes you worried or nervous: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
