

#calss header
class _PROMISCUOUS():
	def __init__(self,): 
		self.name = "PROMISCUOUS"
		self.definitions = [u'(of a person) having a lot of different sexual partners or sexual relationships, or (of sexual habits) involving a lot of different partners: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
