

#calss header
class _SCEPTICAL():
	def __init__(self,): 
		self.name = "SCEPTICAL"
		self.definitions = [u'doubting that something is true or useful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
