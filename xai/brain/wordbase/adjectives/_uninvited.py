

#calss header
class _UNINVITED():
	def __init__(self,): 
		self.name = "UNINVITED"
		self.definitions = [u'not invited: ', u'not wanted or asked for: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
