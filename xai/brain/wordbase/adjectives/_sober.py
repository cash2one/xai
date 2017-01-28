

#calss header
class _SOBER():
	def __init__(self,): 
		self.name = "SOBER"
		self.definitions = [u'not drunk or affected by alcohol: ', u'serious and calm: ', u'Clothes or colours that are sober are plain and not bright.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
