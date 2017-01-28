

#calss header
class _ENTHRALLING():
	def __init__(self,): 
		self.name = "ENTHRALLING"
		self.definitions = [u"keeping someone's interest and attention completely: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
