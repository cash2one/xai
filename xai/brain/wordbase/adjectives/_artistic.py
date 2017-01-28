

#calss header
class _ARTISTIC():
	def __init__(self,): 
		self.name = "ARTISTIC"
		self.definitions = [u'relating to art: ', u'able to create or enjoy art: ', u'skilfully and attractively made: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
