

#calss header
class _OPPRESSED():
	def __init__(self,): 
		self.name = "OPPRESSED"
		self.definitions = [u'governed in an unfair and cruel way and prevented from having opportunities and freedom: ', u'worried and uncomfortable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
