

#calss header
class _COMPLEX():
	def __init__(self,): 
		self.name = "COMPLEX"
		self.definitions = [u'involving a lot of different but related parts: ', u'difficult to understand or find an answer to because of having many different parts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
