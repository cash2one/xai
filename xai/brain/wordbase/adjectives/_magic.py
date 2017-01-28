

#calss header
class _MAGIC():
	def __init__(self,): 
		self.name = "MAGIC"
		self.definitions = [u'with special powers: ', u'happening in an unusual or unexpected way, or easily or quickly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
