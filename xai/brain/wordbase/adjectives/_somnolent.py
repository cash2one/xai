

#calss header
class _SOMNOLENT():
	def __init__(self,): 
		self.name = "SOMNOLENT"
		self.definitions = [u'almost sleeping, or causing sleep: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
