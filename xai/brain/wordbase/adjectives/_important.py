

#calss header
class _IMPORTANT():
	def __init__(self,): 
		self.name = "IMPORTANT"
		self.definitions = [u'necessary or of great value: ', u'having great effect or influence: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
