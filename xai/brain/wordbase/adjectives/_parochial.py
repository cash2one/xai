

#calss header
class _PAROCHIAL():
	def __init__(self,): 
		self.name = "PAROCHIAL"
		self.definitions = [u'relating to a parish (= an area that has its own church or priest): ', u'showing interest only in a narrow range of matters, especially those that directly affect yourself, your town, or your country: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
