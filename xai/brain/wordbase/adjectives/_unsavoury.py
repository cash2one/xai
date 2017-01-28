

#calss header
class _UNSAVOURY():
	def __init__(self,): 
		self.name = "UNSAVOURY"
		self.definitions = [u'unpleasant, or morally offensive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
