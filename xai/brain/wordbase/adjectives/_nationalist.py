

#calss header
class _NATIONALIST():
	def __init__(self,): 
		self.name = "NATIONALIST"
		self.definitions = [u'wanting your country to be politically independent: ', u'strongly believing that your country is better than others: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
