

#calss header
class _ADRENAL():
	def __init__(self,): 
		self.name = "ADRENAL"
		self.definitions = [u'used to refer to two glands situated above the kidneys (the adrenal glands)']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
