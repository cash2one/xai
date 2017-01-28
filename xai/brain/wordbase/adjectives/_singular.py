

#calss header
class _SINGULAR():
	def __init__(self,): 
		self.name = "SINGULAR"
		self.definitions = [u'of or relating to the form of a word used when talking or writing about one thing: ', u'of an unusual quality or standard; noticeable: ', u'unusual or strange; not ordinary']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
