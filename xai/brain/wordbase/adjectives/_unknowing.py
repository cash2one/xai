

#calss header
class _UNKNOWING():
	def __init__(self,): 
		self.name = "UNKNOWING"
		self.definitions = [u'not conscious of a particular situation or problem: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
