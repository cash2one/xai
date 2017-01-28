

#calss header
class _VIRTUAL():
	def __init__(self,): 
		self.name = "VIRTUAL"
		self.definitions = [u'almost a particular thing or quality: ', u'Something that is virtual can be done or seen using a computer and therefore without going anywhere or talking to anyone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
