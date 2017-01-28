

#calss header
class _NUPTIAL():
	def __init__(self,): 
		self.name = "NUPTIAL"
		self.definitions = [u'belonging or relating to a marriage or to the state of being married: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
