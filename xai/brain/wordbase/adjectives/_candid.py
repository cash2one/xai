

#calss header
class _CANDID():
	def __init__(self,): 
		self.name = "CANDID"
		self.definitions = [u'honest and telling the truth, especially about something difficult or painful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
