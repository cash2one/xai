

#calss header
class _VANITY():
	def __init__(self,): 
		self.name = "VANITY"
		self.definitions = [u'used to describe something that is done with the aim of getting praise, fame, or approval rather than for serious or good reasons: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
