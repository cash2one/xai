

#calss header
class _VISIONARY():
	def __init__(self,): 
		self.name = "VISIONARY"
		self.definitions = [u'with the ability to imagine how a country, society, industry, etc. will develop in the future: ', u'relating to a religious vision']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
