

#calss header
class _FULFILLED():
	def __init__(self,): 
		self.name = "FULFILLED"
		self.definitions = [u'feeling happy because you are getting everything that you want from life: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
