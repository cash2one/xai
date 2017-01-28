

#calss header
class _VICARIOUS():
	def __init__(self,): 
		self.name = "VICARIOUS"
		self.definitions = [u'experienced as a result of watching, listening to, or reading about the activities of other people, rather than by doing the activities yourself: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
