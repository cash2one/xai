

#calss header
class _WIZENED():
	def __init__(self,): 
		self.name = "WIZENED"
		self.definitions = [u'small and having dry skin with lines in it, especially because of old age: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
