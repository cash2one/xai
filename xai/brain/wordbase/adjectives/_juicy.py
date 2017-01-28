

#calss header
class _JUICY():
	def __init__(self,): 
		self.name = "JUICY"
		self.definitions = [u'Juicy foods contain a lot of juice and are enjoyable to eat: ', u'used to describe information that is especially interesting because it is shocking or personal: ', u'big, important, or of a high quality: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
