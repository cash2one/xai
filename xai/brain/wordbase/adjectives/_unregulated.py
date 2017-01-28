

#calss header
class _UNREGULATED():
	def __init__(self,): 
		self.name = "UNREGULATED"
		self.definitions = [u'An unregulated type of business or activity is not controlled and directed by fixed rules or laws: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
