

#calss header
class _UPSCALE():
	def __init__(self,): 
		self.name = "UPSCALE"
		self.definitions = [u'Upscale goods and products are of very high quality and intended to be bought by people who are quite rich: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
