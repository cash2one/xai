

#calss header
class _DRIVING():
	def __init__(self,): 
		self.name = "DRIVING"
		self.definitions = [u'strong and powerful and therefore causing things to happen: ', u'rain or snow that is falling fast and being blown by the wind: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
