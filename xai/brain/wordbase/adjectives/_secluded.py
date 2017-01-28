

#calss header
class _SECLUDED():
	def __init__(self,): 
		self.name = "SECLUDED"
		self.definitions = [u'quiet, private, and not near people, roads, or buildings: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
