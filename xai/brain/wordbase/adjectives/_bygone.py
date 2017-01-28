

#calss header
class _BYGONE():
	def __init__(self,): 
		self.name = "BYGONE"
		self.definitions = [u'belonging to or happening in a past time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
