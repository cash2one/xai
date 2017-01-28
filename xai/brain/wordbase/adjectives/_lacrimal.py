

#calss header
class _LACRIMAL():
	def __init__(self,): 
		self.name = "LACRIMAL"
		self.definitions = [u'relating to tears from the eyes: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
