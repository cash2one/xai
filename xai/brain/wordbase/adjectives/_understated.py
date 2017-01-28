

#calss header
class _UNDERSTATED():
	def __init__(self,): 
		self.name = "UNDERSTATED"
		self.definitions = [u'not trying to attract attention or impress people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
