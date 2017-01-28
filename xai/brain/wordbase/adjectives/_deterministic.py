

#calss header
class _DETERMINISTIC():
	def __init__(self,): 
		self.name = "DETERMINISTIC"
		self.definitions = [u'believing that everything that happens must happen as it does and could not have happened any other way, or relating to this belief: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
