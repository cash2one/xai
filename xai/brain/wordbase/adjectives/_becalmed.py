

#calss header
class _BECALMED():
	def __init__(self,): 
		self.name = "BECALMED"
		self.definitions = [u'If a ship with sails is becalmed, it cannot move because there is no wind.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
