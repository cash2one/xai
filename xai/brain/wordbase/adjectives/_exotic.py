

#calss header
class _EXOTIC():
	def __init__(self,): 
		self.name = "EXOTIC"
		self.definitions = [u'unusual and exciting because of coming (or seeming to come) from far away, especially a tropical country: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
