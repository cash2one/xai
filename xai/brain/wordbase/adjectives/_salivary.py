

#calss header
class _SALIVARY():
	def __init__(self,): 
		self.name = "SALIVARY"
		self.definitions = [u'relating to saliva (= the liquid produced in the mouth): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
