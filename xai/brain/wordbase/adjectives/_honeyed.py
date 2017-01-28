

#calss header
class _HONEYED():
	def __init__(self,): 
		self.name = "HONEYED"
		self.definitions = [u"used to describe speech or a person's voice when it is gentle and pleasant to listen to, sometimes in a way that is not sincere"]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
