

#calss header
class _NONCHALANT():
	def __init__(self,): 
		self.name = "NONCHALANT"
		self.definitions = [u'behaving in a calm manner, often in a way that suggests you are not interested or do not care: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
