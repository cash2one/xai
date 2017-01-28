

#calss header
class _EPISCOPAL():
	def __init__(self,): 
		self.name = "EPISCOPAL"
		self.definitions = [u'of or relating to a bishop or a Church that is directed by bishops']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
