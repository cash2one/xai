

#calss header
class _INTENT():
	def __init__(self,): 
		self.name = "INTENT"
		self.definitions = [u'giving all your attention to something: ', u'to be determined to do or achieve something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
