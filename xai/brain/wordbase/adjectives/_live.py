

#calss header
class _LIVE():
	def __init__(self,): 
		self.name = "LIVE"
		self.definitions = [u'having life: ', u'(of a performance) broadcast, recorded, or seen while it is happening: ', u'(of a wire) carrying or charged with electricity: ', u'able to explode: ', u'(of a fire, coals, or a match) still burning or able to burn: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
