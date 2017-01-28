

#calss header
class _UNECONOMIC():
	def __init__(self,): 
		self.name = "UNECONOMIC"
		self.definitions = [u'Uneconomic businesses and industries are not making enough profit or are losing money: ', u'Uneconomic processes or activities use more of something than is necessary, causing it to be wasted: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
