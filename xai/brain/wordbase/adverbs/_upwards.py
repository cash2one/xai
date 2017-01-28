

#calss header
class _UPWARDS():
	def __init__(self,): 
		self.name = "UPWARDS"
		self.definitions = [u'towards a higher position, level, or value: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
