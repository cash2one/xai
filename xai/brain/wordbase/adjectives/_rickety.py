

#calss header
class _RICKETY():
	def __init__(self,): 
		self.name = "RICKETY"
		self.definitions = [u'in bad condition and therefore weak and likely to break: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
