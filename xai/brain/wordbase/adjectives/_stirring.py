

#calss header
class _STIRRING():
	def __init__(self,): 
		self.name = "STIRRING"
		self.definitions = [u'A stirring speech or song is one that produces strong, positive emotions.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
