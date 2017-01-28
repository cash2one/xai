

#calss header
class _MOORISH():
	def __init__(self,): 
		self.name = "MOORISH"
		self.definitions = [u'belonging or relating to the group of Muslim people from North Africa who ruled Spain from 711 to 1492: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
