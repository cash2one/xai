

#calss header
class _PERSPICACIOUS():
	def __init__(self,): 
		self.name = "PERSPICACIOUS"
		self.definitions = [u'quick in noticing, understanding, or judging things accurately: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
