

#calss header
class _REPRESSIVE():
	def __init__(self,): 
		self.name = "REPRESSIVE"
		self.definitions = [u'controlling what people do, especially by using force: ', u'preventing people from expressing their feelings']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
