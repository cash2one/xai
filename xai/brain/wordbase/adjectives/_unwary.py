

#calss header
class _UNWARY():
	def __init__(self,): 
		self.name = "UNWARY"
		self.definitions = [u'not conscious of or careful about possible risks and dangers: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
