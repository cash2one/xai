

#calss header
class _HUMONGOUS():
	def __init__(self,): 
		self.name = "HUMONGOUS"
		self.definitions = [u'US spelling of  humungous ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
