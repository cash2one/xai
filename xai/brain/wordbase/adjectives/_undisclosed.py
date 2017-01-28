

#calss header
class _UNDISCLOSED():
	def __init__(self,): 
		self.name = "UNDISCLOSED"
		self.definitions = [u'If official information is undisclosed, it is secret: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
