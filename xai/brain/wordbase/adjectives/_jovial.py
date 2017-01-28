

#calss header
class _JOVIAL():
	def __init__(self,): 
		self.name = "JOVIAL"
		self.definitions = [u'(of a person) friendly and in a good mood, or (of a situation) enjoyable because of being friendly and pleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
