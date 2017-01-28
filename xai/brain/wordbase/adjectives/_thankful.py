

#calss header
class _THANKFUL():
	def __init__(self,): 
		self.name = "THANKFUL"
		self.definitions = [u'happy or grateful because of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
