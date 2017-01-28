

#calss header
class _PUNCTILIOUS():
	def __init__(self,): 
		self.name = "PUNCTILIOUS"
		self.definitions = [u'very careful to behave correctly or to give attention to details: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
