

#calss header
class _JAUNDICED():
	def __init__(self,): 
		self.name = "JAUNDICED"
		self.definitions = [u'judging everything as bad because bad things have happened to you in the past: ', u'looking slightly yellow in colour because of having jaundice: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
