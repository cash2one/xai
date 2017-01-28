

#calss header
class _SLINKY():
	def __init__(self,): 
		self.name = "SLINKY"
		self.definitions = [u"(of women's clothes) made of delicate cloth and fitting the body closely in a way that is sexually attractive: ", u'(of music or dancing) slow and suggesting sex: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
