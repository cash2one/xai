

#calss header
class _RELIGIOUS():
	def __init__(self,): 
		self.name = "RELIGIOUS"
		self.definitions = [u'relating to religion: ', u'having a strong belief in a god or gods: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
