

#calss header
class _DOWNY():
	def __init__(self,): 
		self.name = "DOWNY"
		self.definitions = [u'filled with feathers: ', u'covered with soft thin hair: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
