

#calss header
class _CORINTHIAN():
	def __init__(self,): 
		self.name = "CORINTHIAN"
		self.definitions = [u'of or copying the most decorated of the three styles of ancient Greek building: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
