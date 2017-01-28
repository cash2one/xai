

#calss header
class _NIGGARDLY():
	def __init__(self,): 
		self.name = "NIGGARDLY"
		self.definitions = [u'slight in amount, quality, or effort: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
