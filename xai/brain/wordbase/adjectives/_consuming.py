

#calss header
class _CONSUMING():
	def __init__(self,): 
		self.name = "CONSUMING"
		self.definitions = [u'A consuming emotion is very strong: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
