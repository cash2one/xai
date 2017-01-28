

#calss header
class _POSTED():
	def __init__(self,): 
		self.name = "POSTED"
		self.definitions = [u'to make sure that someone always knows what is happening: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
