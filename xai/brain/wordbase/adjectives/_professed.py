

#calss header
class _PROFESSED():
	def __init__(self,): 
		self.name = "PROFESSED"
		self.definitions = [u'A professed belief is one that someone has made known: ', u'used to refer to a belief or feeling that someone says they have or feel, but is probably not sincere: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
