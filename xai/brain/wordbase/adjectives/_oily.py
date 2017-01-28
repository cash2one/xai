

#calss header
class _OILY():
	def __init__(self,): 
		self.name = "OILY"
		self.definitions = [u'consisting of or similar to oil: ', u'covered in oil or containing a lot of oil: ', u'too friendly and polite in a way that is not sincere']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
