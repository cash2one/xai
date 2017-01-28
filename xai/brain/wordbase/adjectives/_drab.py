

#calss header
class _DRAB():
	def __init__(self,): 
		self.name = "DRAB"
		self.definitions = [u'boring, especially in appearance; having little colour and excitement: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
