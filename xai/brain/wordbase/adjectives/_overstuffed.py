

#calss header
class _OVERSTUFFED():
	def __init__(self,): 
		self.name = "OVERSTUFFED"
		self.definitions = [u'filled with too much material or too many things: ', u'used to describe films, books, etc. that contain too many different things: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
