

#calss header
class _PLEASANT():
	def __init__(self,): 
		self.name = "PLEASANT"
		self.definitions = [u'enjoyable, attractive, friendly, or easy to like: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
