

#calss header
class _PAPAL():
	def __init__(self,): 
		self.name = "PAPAL"
		self.definitions = [u'relating to the position or authority of the Pope (= the leader of the Roman Catholic Church): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
