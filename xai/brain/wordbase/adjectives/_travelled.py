

#calss header
class _TRAVELLED():
	def __init__(self,): 
		self.name = "TRAVELLED"
		self.definitions = [u'used to refer to a journey or route that many/few people travel on', u'used to refer to people who have visited many countries: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
