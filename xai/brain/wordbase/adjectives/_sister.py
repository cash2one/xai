

#calss header
class _SISTER():
	def __init__(self,): 
		self.name = "SISTER"
		self.definitions = [u'belonging to a pair or group of similar and related things, such as businesses, usually owned or operated by the same person or organization: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
