

#calss header
class _TATTY():
	def __init__(self,): 
		self.name = "TATTY"
		self.definitions = [u'old and in bad condition: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
