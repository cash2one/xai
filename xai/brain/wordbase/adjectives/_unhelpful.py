

#calss header
class _UNHELPFUL():
	def __init__(self,): 
		self.name = "UNHELPFUL"
		self.definitions = [u'not improving a difficult situation: ', u'not wanting to help someone, in a way that seems unfriendly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
