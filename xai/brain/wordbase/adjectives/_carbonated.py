

#calss header
class _CARBONATED():
	def __init__(self,): 
		self.name = "CARBONATED"
		self.definitions = [u'A carbonated drink is fizzy because it contains bubbles of carbon dioxide: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
