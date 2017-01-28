

#calss header
class _UNSEEN():
	def __init__(self,): 
		self.name = "UNSEEN"
		self.definitions = [u'not seen or not able to be seen: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
