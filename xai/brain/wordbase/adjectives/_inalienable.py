

#calss header
class _INALIENABLE():
	def __init__(self,): 
		self.name = "INALIENABLE"
		self.definitions = [u'unable to be removed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
