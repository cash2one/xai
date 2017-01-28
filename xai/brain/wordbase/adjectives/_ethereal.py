

#calss header
class _ETHEREAL():
	def __init__(self,): 
		self.name = "ETHEREAL"
		self.definitions = [u'light and delicate, especially in an unnatural way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
