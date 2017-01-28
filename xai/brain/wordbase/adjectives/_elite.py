

#calss header
class _ELITE():
	def __init__(self,): 
		self.name = "ELITE"
		self.definitions = [u'belonging to the richest, most powerful, best-educated, or best-trained group in a society: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
