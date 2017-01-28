

#calss header
class _UNANNOUNCED():
	def __init__(self,): 
		self.name = "UNANNOUNCED"
		self.definitions = [u'If someone arrives unannounced, they arrive suddenly and unexpectedly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
