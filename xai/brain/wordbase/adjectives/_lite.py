

#calss header
class _LITE():
	def __init__(self,): 
		self.name = "LITE"
		self.definitions = [u'used for describing food or drink that contains fewer calories than usual and is therefore less likely to make you fat: ', u'used for describing things that are not serious and that are easy to understand and enjoy: ', u'not as serious or as good quality as the real thing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
